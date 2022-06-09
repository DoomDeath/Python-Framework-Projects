import { Component, OnInit, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-climate',
  templateUrl: './climate.component.html',
  styleUrls: ['./climate.component.scss']
})
export class ClimateComponent implements OnInit {

  @Output()
  mensaje: EventEmitter<boolean>;


  validacion: boolean = false;
  



  constructor() {
    this.mensaje = new EventEmitter();
   
  }

  ngOnInit(): void {
  }

  cambiarTrue() {
    this.validacion = true;
    this.enviarPapi();

  }
  cambiarFalse() {
    this.validacion = false;
    this.enviarPapi();

  }

  enviarPapi() {
    this.mensaje.emit(this.validacion);
  }

}
