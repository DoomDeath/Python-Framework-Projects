import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  mensaje: boolean = false;


  constructor() { }

  ngOnInit(): void {

  }

  recibirMensaje(msj: boolean) {
    this.mensaje = msj;


  }



}
