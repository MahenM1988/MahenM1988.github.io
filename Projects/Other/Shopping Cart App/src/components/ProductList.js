import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';

const ProductList = ({ products, addToCart }) => {
  const [quantities, setQuantities] = useState({}); // Object to track quantities for each product

  const handleQuantityChange = (id, change) => {
    setQuantities((prevQuantities) => {
      const currentQuantity = prevQuantities[id] || 0;
      const newQuantity = Math.max(0, Math.min(currentQuantity + change, products.find(product => product.id === id).available));
      return { ...prevQuantities, [id]: newQuantity };
    });
  };

  return (
    <div>
      {products.map(product => {
        const quantity = quantities[product.id] || 0; // Get current quantity for this product

        return (
          <div key={product.id} className="product-item">
            <h2>{product.name}</h2>
            <p>Price: ${product.price}</p>
            <button onClick={() => handleQuantityChange(product.id, -1)}>
              <FontAwesomeIcon icon={faMinus} />
            </button>
            <span>{quantity}</span>
            <button onClick={() => handleQuantityChange(product.id, 1)}>
              <FontAwesomeIcon icon={faPlus} />
            </button>
            <button onClick={() => {
              if (quantity > 0) {
                addToCart({ ...product, quantity });
                handleQuantityChange(product.id, -quantity); // Reset quantity after adding to cart
              }
            }}>
              <FontAwesomeIcon icon={faPlus} /> Add to Cart
            </button>
          </div>
        );
      })}
    </div>
  );
};

export default ProductList;
