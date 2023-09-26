<template>
	<div class="app">
	  <HorizontalBanner /> <!-- Include the horizontal banner component -->
	  <!-- Sidebar -->
	  <Sidebar />
  
	  <!-- Content -->
	  <router-view />
	  <Dropdown/>
	</div>
  </template>
  
  <script setup>
  import Sidebar from './components/Sidebar.vue';
  import HorizontalBanner from './components/Banner.vue'; // Import the horizontal banner component
  //import Dropdown from './components/Dropdown.vue';
  </script>
  
  <style lang="scss">
  /* Your existing styles here */
  </style>
  
  

<style lang="scss">
:root {
	--primary: #ffffff;
	--primary-alt: #767B91;
	--grey: #87677B;
	--dark: #4824dc;
	--dark-alt: #5a35ed;
	--light: #bbbbbb;	
	--background: #ffffff;
	--sidebar-width: 300px;
}

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Fira sans', sans-serif;
}

body {
	background: var(--background);
}

button {
	cursor: pointer;
	appearance: none;
	border: none;
	outline: none;
	background: none;
}

.app {
	display: flex;

	main {
		flex: 1 1 0;
		padding: 2rem;

		@media (max-width: 1024px) {
			padding-left: 6rem;
		}
	}
}
</style>