import React from 'react'
import HeroSection from './HeroSection/HeroSection'
import BestSellers from './BestSellers/BestSellers'
import Banners from './Banners/Banners'

const HomePage = () => {
    return (
        <div>
            <HeroSection />
            <BestSellers />
            <Banners />
        </div>
    )
}

export default HomePage
