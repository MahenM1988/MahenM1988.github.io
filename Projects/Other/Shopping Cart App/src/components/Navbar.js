import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons';

const Navbar = ({ itemCount, openCart }) => (
  <nav>
    <h1>Shopping Cart App</h1>
    <button onClick={openCart}>
      <FontAwesomeIcon icon={faShoppingCart} /> Cart ({itemCount})
    </button>
  </nav>
);

export default Navbar;
