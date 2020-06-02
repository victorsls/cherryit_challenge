import {Component, OnInit} from '@angular/core';
import {AuthenticationService} from '../services/authentication.service';


@Component({
    selector: 'app-login',
    templateUrl: './login.page.html',
    styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
    form = {username: '', password: ''};

    constructor(private authService: AuthenticationService) {
    }

    ngOnInit() {
    }

    login() {
        this.authService.login(this.form.username, this.form.password);
        this.form = {username: '', password: ''};
    }
}

