
import promo from '../../../assets/promo.mp4';
import './HeroSection.css';

const HeroSection = () => {


    return (
        <div className="hero-container">
            <video src={promo} autoPlay loop muted className="hero-video" />

            <div className="hero-overlay">
                <h1>Sweetness Awaits at CakeOlicious!</h1>
                <p>Freshly baked daily</p>
                <button type='button'>Test The Magic</button>
            </div>
        </div>
    );
};

export default HeroSection;
