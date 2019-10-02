import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { post } from 'selenium-webdriver/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient, private header: HttpHeaders) { }

  signin(username, password){
    const data = {user:username, password: password}
    const header = { headers: new HttpHeaders({'Content-Type':  'application/json',})}
    const url = `http://localhost:5000/login`
    return this.http.post(url, data, header).toPromise();
  }

  
}
