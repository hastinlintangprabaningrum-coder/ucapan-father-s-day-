# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:21:27 2026

@author: Hastin Lintang 
"""
import webbrowser
import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Happy Father's Day, Bernard Bear!</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #f8fafc;
      overflow: hidden;
      padding: 20px;
      user-select: none;
    }

    .card {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 24px;
      padding: 40px 30px;
      max-width: 480px;
      width: 100%;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      position: relative;
      z-index: 10;
    }

    .badge {
      display: inline-block;
      background: rgba(245, 158, 11, 0.2);
      color: #fbbf24;
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 1px;
      margin-bottom: 16px;
      text-transform: uppercase;
    }

    h1 {
      font-size: 1.95rem;
      margin-bottom: 16px;
      color: #ffffff;
      line-height: 1.25;
    }

    h1 span {
      color: #fbbf24;
      display: block;
      margin-top: 4px;
    }

    p {
      font-size: 1.05rem;
      line-height: 1.6;
      color: #cbd5e1;
      margin-bottom: 28px;
    }

    .btn-love {
      background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
      color: white;
      border: none;
      padding: 16px 32px;
      font-size: 1.1rem;
      font-weight: 600;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 10px 25px rgba(225, 29, 72, 0.4);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .btn-love:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 30px rgba(225, 29, 72, 0.6);
    }

    .btn-love:active {
      transform: scale(0.95);
    }

    .edit-name {
      margin-top: 24px;
      font-size: 0.85rem;
      color: #94a3b8;
      cursor: pointer;
      display: inline-block;
      text-decoration: underline;
    }

    .edit-name:hover {
      color: #fbbf24;
    }

    .particle {
      position: fixed;
      pointer-events: none;
      z-index: 20;
      animation: floatUp var(--duration, 3s) ease-out forwards;
    }

    @keyframes floatUp {
      0% {
        opacity: 1;
        transform: translate(0, 0) scale(0.5) rotate(0deg);
      }
      50% {
        opacity: 1;
      }
      100% {
        opacity: 0;
        transform: translate(var(--tx, 0px), -450px) scale(1.3) rotate(var(--rot, 45deg));
      }
    }
  </style>
</head>
<body>

  <div class="card">
    <div class="badge">Special Day</div>
    <h1>Happy Father's Day, <span id="dad-name">Bernard Bear! 🐻❤️</span></h1>
    <p>
      Thank you for all your hard work, endless prayers, and unconditional love. 
      You are my greatest hero and role model. Wishing you endless health and happiness always!
    </p>
    <button class="btn-love" id="btn-send">Send Love & Roses ❤️🌹</button>
    <br>
    <span class="edit-name" id="edit-name">✏️ Edit nickname</span>
  </div>

  <script>
    const icons = ['❤️', '🌹', '💖', '🌷', '💕', '🐻'];
    const btnSend = document.getElementById('btn-send');
    const editNameBtn = document.getElementById('edit-name');
    const dadNameSpan = document.getElementById('dad-name');

    function createParticles(x, y, count = 12) {
      for (let i = 0; i < count; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        particle.innerText = icons[Math.floor(Math.random() * icons.length)];
        
        const offsetX = (Math.random() - 0.5) * 80;
        const offsetY = (Math.random() - 0.5) * 40;
        particle.style.left = `${x + offsetX}px`;
        particle.style.top = `${y + offsetY}px`;
        
        const size = Math.random() * 20 + 20;
        const spreadX = (Math.random() - 0.5) * 300;
        const rotation = (Math.random() - 0.5) * 90;
        const duration = Math.random() * 1.5 + 2;

        particle.style.fontSize = `${size}px`;
        particle.style.setProperty('--tx', `${spreadX}px`);
        particle.style.setProperty('--rot', `${rotation}deg`);
        particle.style.setProperty('--duration', `${duration}s`);

        document.body.appendChild(particle);

        setTimeout(() => {
          particle.remove();
        }, duration * 1000);
      }
    }

    btnSend.addEventListener('click', (e) => {
      e.stopPropagation();
      const rect = btnSend.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top;
      createParticles(centerX, centerY, 18);
    });

    document.body.addEventListener('click', (e) => {
      if (e.target.id !== 'edit-name') {
        createParticles(e.clientX, e.clientY, 8);
      }
    });

    editNameBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const currentText = dadNameSpan.innerText.replace('! 🐻❤️', '');
      const newName = prompt('Enter nickname for Dad:', currentText);
      if (newName && newName.trim() !== '') {
        dadNameSpan.innerText = `${newName.trim()}! 🐻❤️`;
      }
    });
  </script>

</body>
</html>
"""

# Menyimpan menjadi file HTML dan langsung membukanya di browser
nama_file = "happy_fathers_day.html"
with open(nama_file, "w", encoding="utf-8") as file:
    file.write(html_code)

print("Membuka kartu ucapan di browser...")
webbrowser.open("file://" + os.path.realpath(nama_file))