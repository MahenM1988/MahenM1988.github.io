import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMinus, faPlus, faTrash } from '@fortawesome/free-solid-svg-icons';

const Cart = ({ cartItems, updateQuantity, removeFromCart, closeCart }) => {
  const total = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);

  return (
    <div className="cart-popup">
      <h2>Your Cart</h2>
      {cartItems.length === 0 ? (
        <p>No items in the cart</p>
      ) : (
        cartItems.map(item => (
          <div key={item.id} className="cart-item">
            <h3>{item.name}</h3>
            <p>Price: ${item.price}</p>
            <button 
              onClick={() => updateQuantity(item.id, item.quantity - 1)}
              disabled={item.quantity === 0} // Disable button if quantity is 0
            >
              <FontAwesomeIcon icon={faMinus} />
            </button>
            <span>{item.quantity}</span>
            <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>
              <FontAwesomeIcon icon={faPlus} />
            </button>
            <button onClick={() => removeFromCart(item.id)}>
              <FontAwesomeIcon icon={faTrash} />
            </button>
          </div>
        ))
      )}
      <h3>Total: ${total}</h3>
      <button onClick={closeCart}>Continue Shopping</button>
    </div>
  );
};

export default Cart;
