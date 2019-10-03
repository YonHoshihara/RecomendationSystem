import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/userService/user.service'
import { ActivatedRoute } from '@angular/router'

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  username:string
  resultList

  constructor(private userService: UserService, 
              private activatedRoute: ActivatedRoute) { 
    this.activatedRoute.params.subscribe(p => {
      console.log("username q veio na rota",p.username)
      this.username = p.username;
    })
  }

  ngOnInit() {
    this.userService.getServices().subscribe(
      result => {
        console.log(result)
        this.resultList = result;
      }
    )
  }

  recommend(service){
    this.userService.recommend(this.username,service).subscribe(
      result => {
        this.resultList = result;
      }
    )
  }

}
