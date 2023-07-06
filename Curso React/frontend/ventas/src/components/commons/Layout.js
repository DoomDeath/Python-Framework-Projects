import React from 'react'
import Menu from './Menu';
import Header from './Header';

const Layout = () => {
    return ( 
        <div>
            <Header />
            <div className="container">
                <div className="columns">
                    <div className="column is-one-quarter"><Menu/></div>
                    <div className="column">Contenido</div>
                    <div className="column">Contenido</div>
                </div>

            </div>
        </div>
     
    );
}
 
export default Layout;