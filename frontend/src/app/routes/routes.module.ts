import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SearchComponent } from '../search/search.component';

const routes: Routes = [
  {path: 'search/:username', component:SearchComponent}
]

@NgModule({
  exports: [
    RouterModule
  ],
  imports: [
    RouterModule.forRoot(routes,{anchorScrolling: 'enabled', scrollPositionRestoration: 'enabled'})
  ]
})
export class RoutesModule {}
