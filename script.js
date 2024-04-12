      // When the DOM is fully loaded
      document.addEventListener('DOMContentLoaded', function() {
          // Get the element by its ID
          var element = document.getElementById("projects");

          // Change color when the mouse hovers over it
          element.addEventListener('mouseover', function() {
              this.style.color = 'blue'; // Change to any color you like
          });

          // Revert to the original color when the mouse moves away
          element.addEventListener('mouseout', function() {
              this.style.color = 'black'; // Change back to the original color
          });
      });
