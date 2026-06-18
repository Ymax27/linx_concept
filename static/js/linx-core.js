document.addEventListener('DOMContentLoaded', () => {
  const cursor = document.getElementById('cursor');
  if (cursor) {
    document.addEventListener('mousemove', (e) => {
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
    });
  }

  const loader = document.getElementById('loader');
  if (loader) {
    window.addEventListener('load', () => {
      let progress = 0;
      const progressBar = document.getElementById('progress-bar');
      const statusText = document.getElementById('status-text');

      const interval = setInterval(() => {
        progress += Math.floor(Math.random() * 15) + 5;
        if (progress >= 100) {
          progress = 100;
          clearInterval(interval);
          setTimeout(() => {
            loader.style.opacity = '0';
            loader.style.pointerEvents = 'none';
          }, 500);
        }
        if (progressBar) progressBar.style.width = progress + '%';
        if (statusText) statusText.innerText = progress.toString().padStart(2, '0') + '%';
      }, 100);
    });
  }

  const scrollProgress = document.getElementById('scroll-progress');
  if (scrollProgress) {
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const b = document.body;
      const st = 'scrollTop';
      const sh = 'scrollHeight';
      const percent = ((h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight)) * 100;
      scrollProgress.style.transform = `scaleX(${percent / 100})`;
    });
  }

  document.querySelectorAll('pre code').forEach((el) => {
    if (!el.className.includes('language-')) el.classList.add('language-python');
    if (typeof Prism !== 'undefined') Prism.highlightElement(el);
  });
});
