import React, { useEffect, useState } from 'react';
import './NavigationBar.css';
import { FaUser, FaHeart, FaShoppingCart, FaSearch } from 'react-icons/fa';
import logo from '../../assets/logo.png';

const NavigationBar = () => {
    const [isSticky, setIsSticky] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            const topNavHeight = 80;
            if (window.scrollY > topNavHeight) {
                setIsSticky(true);
            } else {
                setIsSticky(false);
            }
        };

        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-light bg-light position-relative">
                <div className="container position-relative p-3">
                    
                    <div className="navbar-brand position-absolute start-50 translate-middle-x" href="#">
                        <a href="#hh" className="text-decoration-none">
                            <span href="#" className='cursor-pointer'>
                                <img src={logo} alt="CakeOlicious" width={75} height={75} />
                                akeOlicious
                            </span>
                        </a>
                    </div>

                    
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarContent"
                        aria-controls="navbarContent"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    
                    <div className="collapse navbar-collapse w-100" id="navbarContent">
                        <div className="d-flex justify-content-between w-100 flex-column flex-lg-row align-items-center gap-3 mt-3 mt-lg-0">

                            
                            <form className="d-flex search-form" role="search">
                                <div className="search-container">
                                    <FaSearch className="search-icon" />
                                    <input
                                        className="form-control search-input"
                                        type="search"
                                        placeholder="Search..."
                                        aria-label="Search"
                                    />
                                </div>
                            </form>

                            
                            <div className="d-flex align-items-center gap-4">
                                <a href="#" className="nav-link d-flex flex-column align-items-center">
                                    <FaUser size={20} />
                                    <span className="icon-text">Account</span>
                                </a>
                                <a href="#" className="nav-link d-flex flex-column align-items-center">
                                    <FaHeart size={20} />
                                    <span className="icon-text">Wishlist</span>
                                </a>
                                <a href="#" className="nav-link d-flex flex-column align-items-center">
                                    <FaShoppingCart size={20} />
                                    <span className="icon-text">Cart</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>

            <div className={`lower-nav ${isSticky ? 'sticky' : ''}`}>
                <div className="container">
                    <div className="row justify-content-center align-items-center">
                        <div className="col-auto">
                            <ul className="nav-links d-flex gap-4 mb-0">
                                <li><a href="#" className="nav-link">Home</a></li>
                                <li><a href="#" className="nav-link">Chocolates</a></li>
                                <li><a href="#" className="nav-link">Cakes</a></li>
                                <li><a href="#" className="nav-link">Juices</a></li>
                                <li><a href="#" className="nav-link">About Us</a></li>
                            </ul>
                        </div>
                        <div className="col-auto ms-4">
                            <button className="btn btn-primary">Contact Us</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default NavigationBar;
