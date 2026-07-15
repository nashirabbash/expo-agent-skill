#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const targetDir = path.join(process.cwd(), '.agents', 'skills', 'expo-agent');

console.log('🔄 Menginstal expo-agent skill...');

try {
  fs.mkdirSync(targetDir, { recursive: true });

  const packageDir = path.join(__dirname, '..');

  function copyDir(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    let entries = fs.readdirSync(src, { withFileTypes: true });

    for (let entry of entries) {
      let srcPath = path.join(src, entry.name);
      let destPath = path.join(dest, entry.name);

      if (entry.isDirectory()) {
        copyDir(srcPath, destPath);
      } else {
        fs.copyFileSync(srcPath, destPath);
      }
    }
  }

  // Copy files
  fs.copyFileSync(path.join(packageDir, 'SKILL.md'), path.join(targetDir, 'SKILL.md'));
  
  if (fs.existsSync(path.join(packageDir, 'README.md'))) {
    fs.copyFileSync(path.join(packageDir, 'README.md'), path.join(targetDir, 'README.md'));
  }

  // Copy directories
  copyDir(path.join(packageDir, 'reference'), path.join(targetDir, 'reference'));
  copyDir(path.join(packageDir, 'scripts'), path.join(targetDir, 'scripts'));

  console.log('✅ Berhasil menginstal expo-agent skill ke dalam .agents/skills/expo-agent/');
  console.log('📖 Panduan: Agen AI Anda sekarang akan otomatis menggunakan referensi dokumentasi Expo offline sebelum menulis kode.');
} catch (err) {
  console.error('❌ Gagal menginstal skill:', err.message);
  process.exit(1);
}
