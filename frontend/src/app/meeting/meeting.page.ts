import {Component, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {AuthenticationService} from '../services/authentication.service';
import {environment} from '../../environments/environment';

@Component({
    selector: 'app-meeting',
    templateUrl: './meeting.page.html',
    styleUrls: ['./meeting.page.scss'],
})
export class MeetingPage implements OnInit {
    meetings: any = [];

    constructor(private http: HttpClient, private authService: AuthenticationService) {
    }

    ngOnInit() {
        this.getMeetings();
    }

    getMeetings() {
        this.authService.getToken().then(token => {
            const headers = {
                headers: new HttpHeaders().set('Authorization', `Token ${token}`)
            };
            this.http.get(`${environment.api_url}/meetings/`, headers).subscribe((response) => {
                this.meetings = response;
            });
        });
    }

    logout() {
        this.authService.logout();
    }
}
