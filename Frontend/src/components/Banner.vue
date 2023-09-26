<template>
  <div class="horizontal-banner">
    <!-- Your horizontal banner content goes here -->
    <p class="banner-text" ref="typewriterText">
      <span id="cursor" class="cursor">|</span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'HorizontalBanner',
  mounted() {
    const text = '</Stock.Tikkur>'; // The text you want to type
    const speed = 75; // Typing speed in milliseconds
    this.typeWriterEffect(text, speed);
  },
  methods: {
    typeWriterEffect(text, speed) {
      const bannerText = this.$refs.typewriterText;
      const cursor = document.getElementById('cursor'); // Get the cursor element
      let i = 0;
      let isDeleting = false; // Initialize as typing mode, not deleting

      // Initially set the cursor to be visible
      cursor.style.visibility = 'visible';

      function type() {
        const currentText = isDeleting
          ? text.substring(0, i - 1)
          : text.substring(0, i);

        bannerText.textContent = currentText;

        // Toggle the visibility of the cursor
        cursor.style.visibility = i === text.length || isDeleting ? 'hidden' : 'visible';

        if (!isDeleting) {
          i++;
        }

        if (i <= text.length && !isDeleting) {
          setTimeout(type, speed);
        } else {
          isDeleting = true; // Switch to deleting mode
          setTimeout(type, 500); // Pause before starting to delete
        }
      }

      type();
    },
  },
};
</script>

<style scoped>
/* Add your horizontal banner styles here */
.horizontal-banner {
  background-color: #adbce6;
  text-align: left; /* Align text to the left */
  width: 100%;
  height: 100px; /* Set a fixed height for the banner */
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999;
  overflow: hidden; /* Hide overflowing content */
}

.banner-text {
  margin-top: 15px;
  margin-left: 20px;
  font-family: 'Segoe UI', sans-serif; /* Use Segoe UI font */
  color: #fff;
  font-size: 48px;
  font-weight: bold;
  white-space: nowrap; /* Prevent text from wrapping */
  position: relative; /* Set position to relative for absolute positioning of cursor */
}

.cursor {
  position: absolute;
  top: 0;
  right: -10px; /* Adjust the position of the cursor */
  font-size: 48px; /* Adjust cursor size if needed */
  color: #fff; /* Cursor color */
}
</style>
