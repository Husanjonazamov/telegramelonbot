document.addEventListener("DOMContentLoaded", function() {
  // Sonlarni sanash funksiyasi
  const counters = document.querySelectorAll('.count');
  counters.forEach(counter => {
      counter.innerText = '0';
      const updateCounter = () => {
          const target = +counter.getAttribute('data-count');
          const count = +counter.innerText;
          const increment = target / 200;

          if (count < target) {
              counter.innerText = Math.ceil(count + increment);
              setTimeout(updateCounter, 10);
          } else {
              counter.innerText = target;
          }
      };
      updateCounter();
  });
});
