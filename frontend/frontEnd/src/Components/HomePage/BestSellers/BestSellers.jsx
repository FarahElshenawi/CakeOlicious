import React from 'react';
import './BestSellers.css';
import { IMAGES } from '../../../assets/assets';
import Slider from 'react-slick';

const BestSellers = () => {
    const bestSellers = [
        { id: 1, name: 'Product 1', image: IMAGES.cake },
        { id: 2, name: 'Product 2', image: IMAGES.cubcake },
        { id: 3, name: 'Product 3', image: IMAGES.choco },
        { id: 4, name: 'Product 4', image: IMAGES.cake2 },
        { id: 5, name: 'Product 5', image: IMAGES.juice },
    ];
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                },
            },
        ],
    };

    return (
        <div className="container py-4">
            <div className="d-flex flex-column align-items-center">
                <h2 className="text-dark text-center mb-4">Best Sellers</h2>
                <p>Loved by Sweet Tooths Everywhere</p>
            </div>

            <div className="px-3">
                <Slider {...settings}>
                    {bestSellers.map((item) => (
                        <div key={item.id} className="carousel-card">
                            <div className="card">
                                <img src={item.image} alt={item.name} className="card-img-top" />
                                <div className="card-body">
                                    <h5 className="card-title text-center">{item.name}</h5>
                                </div>
                            </div>
                        </div>
                    ))}
                </Slider>
            </div>
        </div>
    );
};

export default BestSellers;