import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  signin(username, password): Observable<any>{
    const body = new HttpParams();
    body.set('username', username)
    body.set('password', password)
    /*const header = new HttpHeaders()
    header.set('Content-Type','application/JSON')*/
    const url = `http://192.168.240.33:5000/login`
    console.log("chamou service")
    return this.http.post(url, body.toString());
  }

  getServices(): Observable<any>{
    /*const header = new HttpHeaders()
    header.set('Content-Type','application/JSON')*/
    const url = `http://192.168.240.33:5000/getservices`
    const body = new HttpParams();
    body.set('teste', 'teste')
    return this.http.post(url,body.toString());
  }

  recommend(username:string, service:string): Observable<any>{
    const body = new HttpParams();
    body.set('username', username)
    body.set('service', service)
    /*const header = new HttpHeaders()
    header.set('Content-Type','application/JSON')*/
    const url = `http://192.168.240.33:5000/recomend`
    return this.http.post(url, body.toString());
  }

  evaluate(username, service, evaluation_element, point, iscompany): Observable<any>{
    const body = new HttpParams();
    body.set('username', username)
    body.set('service', service)
    body.set('evaluation_element', evaluation_element)
    body.set('point', point)
    body.set('iscompany', iscompany)
    /*const header = new HttpHeaders()
    header.set('Content-Type','application/JSON')*/
    const url = `http://192.168.240.33:5000/evaluate`
    return this.http.post(url, body.toString());
  } 
}
