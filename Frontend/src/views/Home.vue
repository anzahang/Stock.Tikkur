<template>
  <main class="home-page">
    <div class="button-container">
      <div class="button-row">
        <router-link to="/about">
          <button class="custom-button button-1" type="button"></button>
        </router-link>
        <router-link to="/deposits">
          <button class="custom-button button-2" type="button"></button>
        </router-link>
      </div>
      <div class="button-row">
        <router-link to="/withdrawals">
          <button class="custom-button button-3" type="button"></button>
        </router-link>
        <router-link to="/holdings">
          <button class="custom-button button-4" type="button"></button>
        </router-link>
      </div>
    </div>
  </main>
</template>

<style scoped>
.custom-button {
  background-color: #4824dc;
  color: white;
  font-size: 24px;
  margin: 30px; /* Add margin for spacing between buttons */
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 1s ease-in-out, box-shadow 0.3s ease-in-out;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.button-1 {
  padding: 160px 390px; /* Adjust padding for Button 1 */
}

.button-2 {
  padding: 160px 310px; /* Adjust padding for Button 2 */
}

.button-3 {
  padding: 160px 310px; /* Adjust padding for Button 3 */
}

.button-4 {
  padding: 160px 390px; /* Adjust padding for Button 4 */
}

.custom-button:focus {
  outline: none;
}

.custom-button:hover {
  background-color: #5a35ed;
}

.button-container {
  text-align: center;
  margin-top: 110px; /* Add margin to shift buttons down */
}

.button-row {
  display: flex;
  justify-content: center;
}
</style>
