import React from 'react'
import Menu from './Menu';
import Header from './Header';

const Layout = (props) => {
    return ( 
        <div>
            <Header />
            <br />
            <div className="container">
                <div className="columns">
                    <div className="column is-one-quarter"><Menu/></div>
                    <div className="column">{props.children}</div>
                </div>
            </div>
        </div>
        );
}
 
export default Layout;