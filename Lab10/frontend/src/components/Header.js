import React from "react";
import Typical from 'react-typical'

const Header = () => (
    <div className="myHeader">    
        <div className="typical">         
            <Typical
                steps={['Scheduler', 500,
                ]}
                loop={Infinity}
            />            
        </div> 
    </div>
);

export default Header;