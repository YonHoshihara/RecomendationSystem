import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/userService/user.service'
import { Router } from '@angular/router'

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.css']
})
export class ContentComponent implements OnInit {

  constructor(private userService: UserService, private router:Router) { }

  ngOnInit() {
  }

  signin(username:string, password:string){
    console.log("chamou signin")
    this.userService.signin(username,password).subscribe(
      result => {
        console.log(result)
        if(result){
          var url = 'search/:'+username
          this.router.navigate([url])
        }
      }
    )
  }

}
