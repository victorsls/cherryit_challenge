import {Injectable} from '@angular/core';
import {Router} from '@angular/router';
import {ToastController, Platform} from '@ionic/angular';
import {BehaviorSubject} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {StorageService} from './storage.service';
import {environment} from '../../environments/environment';


@Injectable()
export class AuthenticationService {

    authState = new BehaviorSubject(false);

    constructor(
        private router: Router, private storage: StorageService, private platform: Platform,
        public toastController: ToastController, private http: HttpClient) {
        this.platform.ready().then(() => {
            this.ifLoggedIn();
        });
    }

    ifLoggedIn() {
        this.storage.getObject('token').then((response) => {
            if (response) {
                this.authState.next(true);
            }
        });
    }


    login(username, password) {
        const headers = {headers: new HttpHeaders().set('Content-Type', 'application/json')};
        const body = {username, password};
        this.http.post(`${environment.api_url}/login/`, body, headers).subscribe((response: any) => {
            this.authState.next(true);
            this.storage.setObject('token', response.token);
            this.router.navigate(['/meeting']);
        }, error => {
            console.log(error);
        });
    }

    logout() {
        this.storage.removeItem('token').then(() => {
            this.router.navigate(['login']);
            this.authState.next(false);
        });
    }

    isAuthenticated() {
        return this.authState.value;
    }

    getToken() {
        return this.storage.getObject('token');
    }
}
