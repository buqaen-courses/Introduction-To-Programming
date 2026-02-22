# Data Representation: Turning Everything into Numbers

## Introduction: The Universal Translator

Imagine you have a magic box that can only understand numbers. Now give it:
- A letter from a friend
- A photo of your vacation
- Your favorite song
- A movie

Amazingly, the box can store and work with ALL of these! How? By converting everything into numbers. This is **data representation** - the art of translating the world into a language computers understand.

---

## Why Numbers?

### The Computer's Native Language

Computers are essentially very fast calculators. They excel at:
- Storing numbers
- Comparing numbers
- Adding, subtracting, multiplying numbers

So we translate everything into numbers, and the computer can handle it!

### Real-World Analogy: A Library System

Think of a library:
- Each book has a **call number** (like QA76.5 .C67)
- The number represents: subject, author, title
- With the number system, you can organize millions of books

Data representation works the same way - we create "call numbers" for everything!

---

## Representing Text: From Letters to Numbers

### The Idea: Assign a Number to Every Character

Imagine creating a secret code:
- A = 1, B = 2, C = 3...
- Space = 0, ! = 27, ? = 28...

Computers use standardized codes so everyone agrees.

### ASCII: The Original English Code

**ASCII** (American Standard Code for Information Interchange) was created in the 1960s:

```
'A' = 65  = 01000001
'B' = 66  = 01000010
'C' = 67  = 01000011
'a' = 97  = 01100001
'0' = 48  = 00110000
' ' = 32  = 00100000
```

**ASCII can represent:**
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Punctuation (!@#$% etc.)
- Control codes (tab, newline, etc.)

**Total: 128 characters** (uses 7 bits, but often stored in 8)

### Example: "HELLO" in ASCII

```
Letter    Binary      Decimal
H    →  01001000  →  72
e    →  01100101  →  101
l    →  01101100  →  108
l    →  01101100  →  108
o    →  01101111  →  111

"HELLO" = 5 bytes = 40 bits
```

### Unicode: World's Languages United

ASCII only covers English. What about:
- Arabic? مرحبا
- Chinese? 你好
- Emoji? 😀🎉❤️
- Russian? Привет

**Unicode** assigns a unique number to EVERY character in EVERY language:
- Over 140,000 characters defined
- Each has a "code point" like U+0041 (A), U+0627 (ا)

### UTF-8: Smart Storage for Unicode

Unicode needs many bits, but most text uses common characters. **UTF-8** solves this:

| Character Type | Bytes Used | Example |
|----------------|------------|---------|
| English ASCII | 1 byte | "A" |
| European accents | 2 bytes | "é" |
| Asian languages | 3 bytes | "中" |
| Emoji, rare symbols | 4 bytes | "😀" |

**Benefits:**
- English text stays small (1 byte per character)
- Can still represent all world languages
- Backward compatible with old ASCII files

---

## Representing Numbers: Binary

### Counting with Light Switches

We use decimal (0-9) because we have 10 fingers. Computers use binary (0-1) because they have electronic switches.

**Binary place values:**
```
Position:  7   6   5   4   3   2   1   0
Value:   128  64  32  16   8   4   2   1

Example:  0   1   0   0   1   0   0   1
          0 + 64 + 0 + 0 + 8 + 0 + 0 + 1 = 73
```

### Practice: Binary to Decimal

| Binary | Calculation | Decimal |
|--------|-------------|---------|
| 00000001 | 1 | 1 |
| 00000010 | 2 | 2 |
| 00000100 | 4 | 4 |
| 00001000 | 8 | 8 |
| 00001001 | 8+1 | 9 |
| 00010000 | 16 | 16 |
| 00101010 | 32+8+2 | 42 |

### Integer Types: How Big Can We Count?

| Type | Bits | Min Value | Max Value |
|------|------|-----------|-----------|
| Byte | 8 | 0 | 255 |
| Short | 16 | 0 | 65,535 |
| Integer | 32 | -2 billion | +2 billion |
| Long | 64 | -9 quintillion | +9 quintillion |

**Example uses:**
- Byte: Single character, small color value
- Integer: Counting things, most calculations
- Long: Timestamps, very large numbers

### Decimal Numbers (Floating Point)

For numbers like 3.14159 or 0.001, computers use **floating point**:

```
Similar to scientific notation: 1.23 × 10⁵
Computer stores: Sign + Exponent + Mantissa

Example: 3.14159
→ Stored as special binary pattern
→ Can represent very large and very small numbers
```

**Important note:** Some decimals can't be represented exactly:
```
0.1 + 0.2 = 0.30000000000000004  (not exactly 0.3!)
```
This is like how 1/3 = 0.333... in decimal - it never ends!

---

## Representing Images: Pixels and Colors

### The Concept: Mosaic of Colored Dots

An image is like a **mosaic** made of tiny colored tiles called **pixels** (picture elements).

**Key idea:** If the pixels are small enough, your eye blends them into a smooth image!

### Resolution: How Many Pixels?

| Resolution | Pixels | Description |
|------------|--------|-------------|
| 640×480 | 307,200 | Old computer screen |
| 1920×1080 (Full HD) | 2,073,600 | Standard TV/monitor |
| 3840×2160 (4K) | 8,294,400 | High-end TV |
| 12 MP (phone photo) | 12,000,000 | Typical smartphone |

**Analogy:** Resolution is like thread count in fabric. More threads = smoother fabric. More pixels = smoother image.

### Color Representation: RGB

Every color is made by mixing **Red, Green, and Blue** light:

```
Pure Red:   Red=255, Green=0,   Blue=0
Pure Green: Red=0,   Green=255, Blue=0
Pure Blue:  Red=0,   Green=0,   Blue=255
Yellow:     Red=255, Green=255, Blue=0  (Red + Green)
White:      Red=255, Green=255, Blue=255 (All on)
Black:      Red=0,   Green=0,   Blue=0   (All off)
```

Each color component uses **8 bits** (0-255), so one pixel = **24 bits** (3 bytes).

**Color Examples:**
```
Orange:     255, 165, 0
Pink:       255, 192, 203
Purple:     128, 0, 128
Sky Blue:   135, 206, 235
```

### Example: Calculate Image Size

A 1920×1080 photo:
```
Pixels: 1920 × 1080 = 2,073,600 pixels
Bytes per pixel: 3 (RGB)
Total bytes: 2,073,600 × 3 = 6,220,800 bytes
Total megabytes: ~6 MB
```

### Transparency: RGBA

For images with transparency (like PNGs), we add an **Alpha** channel:
```
RGBA = Red, Green, Blue, Alpha (transparency)
Alpha: 0 = fully transparent, 255 = fully opaque
```

Now each pixel uses **4 bytes**.

---

## Representing Sound: Sampling Waves

### The Concept: Connecting Dots

Sound is a wave. To digitize it:
1. Take thousands of "snapshots" per second (sampling)
2. Record the height of the wave at each snapshot
3. Store those heights as numbers

**Key insight:** More snapshots = more accurate sound!

### Audio Terms Explained

| Term | Meaning | Example |
|------|---------|---------|
| **Sample Rate** | Snapshots per second | 44,100 Hz (CD quality) |
| **Bit Depth** | Precision of each snapshot | 16 bits (65,536 levels) |
| **Channels** | Mono (1) or Stereo (2) | Stereo = left + right |

### Calculate Audio File Size

A 3-minute song at CD quality:
```
Formula: sample_rate × bit_depth × channels × seconds

44,100 × 16 × 2 × 180 = 254,016,000 bits
                    = 31,752,000 bytes
                    ≈ 30 MB (uncompressed)
```

MP3 compression reduces this to ~3-5 MB!

### Visual: Sampling a Sound Wave

```
Original analog wave:
    ～～～～～～～～～～

Sampled (digital) version:
    ·  ·  ·  ·  ·  ·  ·
    │  │  │  │  │  │  │
────┴──┴──┴──┴──┴──┴──┴───

When played back, the steps are smoothed out!
```

---

## Representing Video: Images Over Time

### The Concept: Flipbook Animation

Video is just many images shown rapidly:
- **24 fps**: Cinematic look
- **30 fps**: Standard TV
- **60 fps**: Smooth, video game look

Each frame is a digital image (like we discussed above).

### Calculate Video Size

One second of 1080p video:
```
Frame size: 1920 × 1080 × 3 bytes = 6.2 MB
At 30 fps: 6.2 MB × 30 = 186 MB/second!
One minute: 186 × 60 = 11,160 MB ≈ 11 GB!
```

**Without compression**, video files would be enormous!

---

## Data Compression: Making Files Smaller

### Why Compress?

| Media Type | Uncompressed | Compressed | Savings |
|------------|--------------|------------|---------|
| 3-min song | 30 MB | 3 MB (MP3) | 90% |
| Photo | 6 MB | 500 KB (JPEG) | 92% |
| 1-min video | 11 GB | 100 MB (MP4) | 99% |

### Lossless Compression: Perfect Reconstruction

Like a zipped file - you get exactly the original back.

**Techniques:**
- **Run-length encoding**: "AAAAA" → "5A"
- **Dictionary methods**: Replace repeated patterns with short codes

**Formats:** PNG, GIF, ZIP, FLAC

### Lossy Compression: Good Enough Quality

Removes data humans won't notice.

**Example - MP3 Audio:**
- Removes very high frequencies (most adults can't hear them)
- Uses "perceptual coding" - keeps what we hear, removes what we don't
- Quality setting determines how much is removed

**Example - JPEG Images:**
- Smooths subtle color changes
- Keeps edges sharp (what we notice)
- Quality 90% looks the same as 100% to most people

### The Quality vs Size Trade-off

```
JPEG Quality Settings:

Quality 100%: 5 MB  ━━━━━━━━━━━━  Perfect, but large
Quality 90%:  1 MB  ━━            Looks the same!
Quality 50%:  300 KB             Slight artifacts visible
Quality 10%:  50 KB  ░░░░░░░░    Blocky, poor quality
```

---

## Practice: Calculate Data Sizes

### Exercise 1: Text File Size
How many bytes to store this sentence?
```
"Hello, World!"
```

(Answer: Count characters including spaces and punctuation)

### Exercise 2: Image Size
Calculate the uncompressed size of a 4K photo (3840×2160 pixels):
- At 24-bit color depth: _______ MB
- At 32-bit color depth (RGBA): _______ MB

### Exercise 3: Audio File Size
A 5-minute podcast episode in CD quality:
- Uncompressed size: _______ MB
- After MP3 compression (1/10 size): _______ MB

---

## Key Takeaways

1. **Everything becomes numbers**: Text, images, sound, video - all converted to binary
2. **Text uses character codes**: ASCII for English, Unicode for world languages
3. **Images are pixel grids**: Each pixel has RGB color values
4. **Sound is sampled waves**: Thousands of measurements per second
5. **Compression reduces size**: Lossless keeps all data, lossy keeps what matters

## Remember

- **Text** → Character codes → Binary
- **Numbers** → Binary representation
- **Images** → Pixels with RGB values
- **Sound** → Sampled wave heights
- **Video** → Many images per second
- **Compression** → Smaller files (sometimes with quality trade-offs)

---

## Next Steps

- Learn specific file formats (JPEG, PNG, MP3, MP4)
- Understand compression algorithms in detail
- Explore binary arithmetic and bit manipulation
