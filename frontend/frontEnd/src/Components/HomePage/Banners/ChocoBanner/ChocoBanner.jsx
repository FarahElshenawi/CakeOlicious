import React from 'react';
import './ChocoBanner.css';
import choco from '../../../../assets/choco.png';
import { Slide } from "react-awesome-reveal"
const ChocoBanner = () => {
    return (
        <div className="cont">
            <div className="container">
                <div className="row d-flex justify-content-around align-items-center">
                    <Slide direction='left' className='col-6 text-section d-flex flex-column justify-content-center align-items-center'>
                        <div className="d-flex flex-column align-items-center">
                            <h2>Our Chocolate Obsession</h2>
                            <p>Handcrafted with Love</p>
                            <button type="button">Shop Now</button>
                        </div>
                    </Slide>
                    <Slide direction='right' className="col-6 choco-image" ><img src={choco} alt="Chocolate" /></Slide>
                </div>
            </div>
        </div>
    );
};

export default ChocoBanner;