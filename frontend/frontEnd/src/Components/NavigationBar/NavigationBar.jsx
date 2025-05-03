import React from 'react';
import './NavigationBar.css'
import { FaUser, FaHeart, FaShoppingCart } from 'react-icons/fa';

const NavigationBar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid d-flex align-items-center">
                {/* Search on the left */}
                <div className="d-flex align-items-center">
                    <form className="d-flex align-items-center" role="search">
                        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                        <button className="btn btn-outline-success" type="submit">Search</button>
                    </form>
                </div>

                {/* Brand in the middle */}
                <a className="navbar-brand position-absolute start-50 translate-middle-x" href="#">CakeOlicious</a>

                {/* Icons on the right */}
                <div className="d-flex align-items-center gap-3">
                    <a href="#" className="nav-link">
                        <FaUser size={20} />
                    </a>
                    <a href="#" className="nav-link">
                        <FaHeart size={20} />
                    </a>
                    <a href="#" className="nav-link">
                        <FaShoppingCart size={20} />
                    </a>
                </div>

                {/* Mobile menu button */}
                <button className="navbar-toggler ms-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
            </div>
        </nav>
    );
};

export default NavigationBar;
