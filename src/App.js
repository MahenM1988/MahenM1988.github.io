
import './App.css';
import React, { useState } from 'react';
import Navbar from './components/Navbar';
import ProductList from './components/ProductList';
import Cart from './components/Cart';
import productsData from './data/products.json';

const App = () => {
  const initialInventory = productsData.map(product => ({ ...product }));
  const [inventory, setInventory] = useState(initialInventory);
  const [cart, setCart] = useState([]);
  const [isCartOpen, setIsCartOpen] = useState(false);

  const addToCart = (product) => {
    const existingItem = cart.find(item => item.id === product.id);
    
    // Check if the item can be added based on available stock
    const totalQuantityInCart = existingItem ? existingItem.quantity : 0;
    const totalQuantityAvailable = inventory.find(item => item.id === product.id).available;

    if (totalQuantityInCart + product.quantity <= totalQuantityAvailable) {
      if (existingItem) {
        const updatedCart = cart.map(item => 
          item.id === product.id 
            ? { ...existingItem, quantity: existingItem.quantity + product.quantity } 
            : item
        );
        setCart(updatedCart);
      } else {
        setCart([...cart, product]);
      }

      // Update the inventory by reducing the available stock
      setInventory(inventory.map(item => 
        item.id === product.id 
          ? { ...item, available: item.available - product.quantity } 
          : item
      ));
    }
  };

  const updateQuantity = (id, quantity) => {
    const itemInCart = cart.find(item => item.id === id);
    
    if (itemInCart) {
      const currentQuantity = itemInCart.quantity;
      const itemAvailable = inventory.find(item => item.id === id).available;
      
      // If quantity decreases, update inventory accordingly
      if (quantity < currentQuantity) {
        const quantityToRemove = currentQuantity - quantity;
        setInventory(inventory.map(item => 
          item.id === id 
            ? { ...item, available: item.available + quantityToRemove } 
            : item
        ));
      } else if (quantity > currentQuantity) {
        // Check if we can increase the quantity in the cart
        if (itemAvailable >= quantity - currentQuantity) {
          setInventory(inventory.map(item => 
            item.id === id 
              ? { ...item, available: item.available - (quantity - currentQuantity) } 
              : item
          ));
        } else {
          return; // Not enough stock available to increase
        }
      }

      setCart(cart.map(item => item.id === id ? { ...item, quantity } : item));
    } else {
      if (quantity < 1) {
        removeFromCart(id);
      }
    }
  };

  const removeFromCart = (id) => {
    const itemInCart = cart.find(item => item.id === id);
    if (itemInCart) {
      setCart(cart.filter(item => item.id !== id));
      // Restore available stock when an item is removed from the cart
      setInventory(inventory.map(item => 
        item.id === id 
          ? { ...item, available: item.available + itemInCart.quantity } 
          : item
      ));
    }
  };

  const toggleCart = () => {
    setIsCartOpen(!isCartOpen);
  };

  return (
    <div>
      <Navbar itemCount={cart.reduce((acc, item) => acc + item.quantity, 0)} openCart={toggleCart} />
      <ProductList products={inventory} addToCart={addToCart} />
      {isCartOpen && <Cart cartItems={cart} updateQuantity={updateQuantity} removeFromCart={removeFromCart} closeCart={toggleCart} />}
    </div>
  );
};

export default App;
