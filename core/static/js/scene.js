/* ============================================================
   NURSES REVISION UGANDA — PARTICLE FIELD ONLY
   ============================================================ */
import * as THREE from 'three';

(function () {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion) return;

  const hero = document.querySelector('.hero');
  if (!hero) {
    console.warn('[3D] .hero not found');
    return;
  }

  /* ---------- Renderer ---------- */
  const renderer = new THREE.WebGLRenderer({
    antialias: true,
    alpha: true,
    powerPreference: 'high-performance'
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(hero.clientWidth, hero.clientHeight);
  renderer.setClearColor(0x000000, 0);

  const canvas = renderer.domElement;
  canvas.style.position = 'absolute';
  canvas.style.inset = '0';
  canvas.style.zIndex = '0';
  canvas.style.pointerEvents = 'none';
  hero.prepend(canvas);

  /* ---------- Scene & camera ---------- */
  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    55,
    hero.clientWidth / hero.clientHeight,
    1,
    2000
  );
  camera.position.set(0, 0, 600);

  /* ---------- Particles ---------- */
  const particleCount = 900;
  const positions = new Float32Array(particleCount * 3);
  const colorsArr = new Float32Array(particleCount * 3);
  const palette = [0x00e5c4, 0x7c6bff, 0xffcb6b, 0xff5ca8];

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3]     = (Math.random() - 0.5) * 2200;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 1400;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 1600 - 300;

    const c = new THREE.Color(palette[i % palette.length]);
    colorsArr[i * 3]     = c.r;
    colorsArr[i * 3 + 1] = c.g;
    colorsArr[i * 3 + 2] = c.b;
  }

  const particleGeo = new THREE.BufferGeometry();
  particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  particleGeo.setAttribute('color', new THREE.BufferAttribute(colorsArr, 3));

  const particles = new THREE.Points(
    particleGeo,
    new THREE.PointsMaterial({
      size: 4,
      vertexColors: true,
      transparent: true,
      opacity: 0.75,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
      sizeAttenuation: true
    })
  );
  scene.add(particles);

  /* ---------- Mouse → camera tilt ---------- */
  let mouseX = 0, mouseY = 0;
  let targetX = 0, targetY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth)  * 2 - 1;
    mouseY = (e.clientY / window.innerHeight) * 2 - 1;
  });

  /* ---------- Resize ---------- */
  window.addEventListener('resize', () => {
    const w = hero.clientWidth;
    const h = hero.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });

  /* ---------- Animate ---------- */
  const clock = new THREE.Clock();

  function animate() {
    const t = clock.getElapsedTime();

    targetX += (mouseX - targetX) * 0.05;
    targetY += (mouseY - targetY) * 0.05;
    camera.position.x = targetX * 80;
    camera.position.y = -targetY * 60;
    camera.lookAt(0, 0, 0);

    particles.rotation.y = t * 0.03;

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }

  animate();

  console.log('%c[NursesRevision] particle field active', 'color:#00e5c4;font-weight:bold');
})();