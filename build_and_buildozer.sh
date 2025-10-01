#!/data/data/com.termux/files/usr/bin/bash
# Miguel AI APK Build Script for Termux

echo "🔧 Setting up zlib headers for Buildozer..."
mkdir -p ~/.buildozer/fake-debs/zlib1g-dev
ln -sf $PREFIX/include/zlib.h ~/.buildozer/fake-debs/zlib1g-dev/zlib.h
ln -sf $PREFIX/include/zconf.h ~/.buildozer/fake-debs/zlib1g-dev/zconf.h

echo "📌 Exporting compiler flags..."
export CFLAGS="-I$PREFIX/include"
export LDFLAGS="-L$PREFIX/lib"

echo "🚀 Starting Buildozer build..."
buildozer -v android debug --ignore-system-checks

echo "✅ Build script finished. Check for APK in ./.buildozer/android/platform/build-arm64/dists/"
