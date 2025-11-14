# 🔧 5 Issues to Fix - Implementation Guide

## Issue 1: Dropdown (DONE ✅)
Sudah di-fix sebelumnya dengan mengubah `overflow: hidden` menjadi `overflow-y: visible` dan z-index menjadi 1000.

---

## Issue 2: Window Terpisah - Welcome Message Sync ❌

### Problem
Ketika membuka 2 tab/window berbeda (customer & admin), welcome message tidak singkron antar window.

### Solution
Gunakan localStorage event listener untuk mendeteksi perubahan di window lain.

### Implementation
Tambahkan di awal `<script>` section kedua file (index.html dan admin.html):

```javascript
// Listen for storage changes from other windows
window.addEventListener('storage', (event) => {
    if (event.key === 'currentUser' || event.key === 'authToken') {
        // Reload user data from storage
        authToken = localStorage.getItem('authToken');
        currentUser = JSON.parse(localStorage.getItem('currentUser'));
        
        // Update welcome message
        if (currentUser && document.getElementById('userName')) {
            const role = currentUser.role === 'admin' ? 'Admin' : 'Customer';
            document.getElementById('userName').textContent = `${role}: ${currentUser.username}`;
        }
    }
});
```

---

## Issue 3: Reload Customer - Jangan Hilang Receipt 📝

### Problem
Ketika reload halaman customer, receipt modal hilang dan data receipt tidak tersimpan.

### Solution
Simpan receipt data di localStorage dan tampilkan kembali saat page load.

### Implementation

**Step 1: Simpan receipt ke localStorage**
Ubah `showReceipt()` function:

```javascript
function showReceipt(orderId, name, email, phone, address, payment, subtotal, tax, total) {
    // Simpan receipt data ke localStorage
    const receiptData = {
        orderId,
        name,
        email,
        phone,
        address,
        payment,
        subtotal,
        tax,
        total,
        items: cart.map(item => ({
            name: item.name,
            quantity: item.quantity,
            price: item.price
        }))
    };
    localStorage.setItem('lastReceipt', JSON.stringify(receiptData));
    
    // Display receipt
    document.getElementById('receiptOrderId').textContent = orderId;
    // ... rest of function
}
```

**Step 2: Restore receipt saat page load**
Tambahkan di init() function:

```javascript
// Initialize
function init() {
    // ... existing code
    
    // Check if there's a last receipt to restore
    const lastReceipt = localStorage.getItem('lastReceipt');
    if (lastReceipt) {
        const receipt = JSON.parse(lastReceipt);
        showReceipt(receipt.orderId, receipt.name, receipt.email, receipt.phone, 
                   receipt.address, receipt.payment, receipt.subtotal, receipt.tax, receipt.total);
    }
}
```

---

## Issue 4: Input QR & Logo 🎨

### Part A: Add Logo to Header

**Step 1: Buat/Upload logo image**
Buat file SVG logo di `frontend/` folder dengan nama `logo.svg`

```svg
<!-- frontend/logo.svg -->
<svg width="40" height="40" viewBox="0 0 40 40" fill="none">
  <!-- Pastry/croissant shape -->
  <path d="M20 5 L30 15 Q30 25 20 35 Q10 25 10 15 Z" fill="#e15f8c"/>
  <path d="M15 12 L25 12 L22 22 L18 22 Z" fill="#6c3f2b" opacity="0.8"/>
</svg>
```

**Step 2: Update HTML untuk menampilkan logo**
Di `index.html` dan `admin.html`, ubah bagian nav:

```html
<nav>
    <div class="nav-brand">
        <img src="logo.svg" alt="Pastry Logo" class="nav-logo">
        <span>🥐 Pastry</span>
    </div>
    <!-- rest of nav -->
</nav>
```

**Step 3: Tambahkan CSS untuk logo**

```css
.nav-logo {
    width: 40px;
    height: 40px;
    margin-right: 10px;
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
```

### Part B: Add QR Code Input untuk Payment

**Step 1: Update Payment Method Select**
Di form delivery details:

```html
<select id="paymentMethod" required>
    <option value="">Select Payment Method</option>
    <option value="cash">Cash on Delivery (COD)</option>
    <option value="qr">QR Payment</option>
    <option value="transfer">Bank Transfer</option>
</select>
```

**Step 2: Tambahkan QR Code Display Section**

```html
<div id="qrSection" style="display: none;">
    <h4>Scan QR Code untuk pembayaran:</h4>
    <div id="qrCodeDisplay" style="text-align: center; padding: 20px;">
        <img id="qrCodeImage" src="" alt="QR Code" style="width: 200px; height: 200px;">
        <p>Scan kode di atas untuk melakukan pembayaran</p>
    </div>
</div>
```

**Step 3: Generate QR Code on Payment Method Change**

```javascript
document.getElementById('paymentMethod').addEventListener('change', function() {
    if (this.value === 'qr') {
        document.getElementById('qrSection').style.display = 'block';
        generateQRCode();
    } else {
        document.getElementById('qrSection').style.display = 'none';
    }
});

function generateQRCode() {
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const tax = subtotal * 0.05;
    const total = subtotal + tax;
    
    // Use QR code API (e.g., qrserver.com)
    const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=PASTRY|${currentUser.username}|${total}`;
    document.getElementById('qrCodeImage').src = qrUrl;
}
```

---

## Issue 5: Remove Gradient, Maximize Shadows ✨

### Problem
Terlalu banyak gradient, perlu lebih clean dan modern dengan shadow effects.

### Solution
Gunakan solid colors dan shadow untuk depth.

### Implementation

**Step 1: Update CSS Variables**

```css
:root {
    --brown-dark: #6c3f2b;
    --pink-light: #f1d2de;
    --pink-vibrant: #e15f8c;
    --brown-medium: #a88076;
    --green-base: #b4d96f;
    --cream: #fef8f1;
    --black: #1a1a1a;
    --white: #ffffff;
    
    /* Shadow variables */
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.15);
    --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.2);
    --shadow-hover: 0 12px 32px rgba(0, 0, 0, 0.25);
}
```

**Step 2: Update Cards - Remove Gradient, Add Shadows**

```css
/* BEFORE - dengan gradient */
.menu-card {
    background: linear-gradient(135deg, #ffffff 0%, #fef8f1 100%);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* AFTER - solid color dengan shadow hover */
.menu-card {
    background-color: var(--white);
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}

.menu-card:hover {
    box-shadow: var(--shadow-hover);
    transform: translateY(-4px);
}
```

**Step 3: Update Buttons**

```css
/* Solid colors, no gradient */
.btn-primary {
    background-color: var(--pink-vibrant);
    color: var(--white);
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}

.btn-primary:hover {
    box-shadow: var(--shadow-hover);
    transform: translateY(-2px);
}

.btn-primary:active {
    transform: translateY(0);
    box-shadow: var(--shadow-sm);
}
```

**Step 4: Update Modal Backgrounds**

```css
/* Remove gradient */
.modal {
    background-color: var(--white);
    box-shadow: var(--shadow-lg);
    border-radius: 12px;
}

.modal-backdrop {
    background-color: rgba(0, 0, 0, 0.5);
}
```

---

## 🎯 Checklist Implementasi

### Issue 2: Window Sync
- [ ] Tambahkan storage event listener di index.html
- [ ] Tambahkan storage event listener di admin.html
- [ ] Test dengan 2 tab membuka file berbeda
- [ ] Verify welcome message update saat login di tab lain

### Issue 3: Receipt Persistence
- [ ] Modifikasi `showReceipt()` untuk save ke localStorage
- [ ] Tambahkan restore receipt logic di `init()`
- [ ] Test: place order → reload page → receipt masih ada
- [ ] Test: close receipt → reload → tidak show receipt (cleared properly)

### Issue 4: QR & Logo
- [ ] Buat/upload logo.svg file
- [ ] Update nav HTML dengan logo
- [ ] Add CSS untuk logo styling
- [ ] Tambahkan payment method select
- [ ] Tambahkan QR code display section
- [ ] Implement QR generation logic
- [ ] Test QR code generation

### Issue 5: Colors & Shadows
- [ ] Audit semua gradient di CSS
- [ ] Replace dengan solid colors dari palette
- [ ] Add shadow variables di :root
- [ ] Update cards dengan shadow hover
- [ ] Update buttons dengan shadow & transform
- [ ] Update modals dengan shadow
- [ ] Test hover effects smooth

---

## 📋 File Priority

### High Priority
1. `frontend/index.html` - Receipt persistence + storage listener + QR + logo
2. `frontend/admin.html` - Storage listener only
3. Create `frontend/logo.svg` - Logo file

### Medium Priority
4. CSS updates - Colors, shadows, no gradients

---

## 🚀 Testing Steps

```bash
# 1. Update files
# 2. Start services
./STARTUP.sh

# 3. Test Issue 2 (Window Sync)
# Open 2 windows: Tab A customer, Tab B admin
# Login at Tab A
# Check Tab B welcome message updates

# 4. Test Issue 3 (Receipt Persistence)
# Place order
# Reload page (Cmd+R)
# Receipt modal should show again

# 5. Test Issue 4 (QR & Logo)
# Logo should appear in navbar
# Select "QR Payment" in form
# QR code should generate

# 6. Test Issue 5 (Shadows)
# Hover over cards
# Should have smooth shadow elevation
# No gradient backgrounds
```

---

**Status**: Ready for implementation ✅
