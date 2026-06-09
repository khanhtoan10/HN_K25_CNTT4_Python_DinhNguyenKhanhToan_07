transactions = []

def classify_scale(amount):
    """Phân loại quy mô dựa trên số tiền thực tế."""
    if amount < 2000000:
        return "Nhỏ"
    elif amount < 10000000:
        return "Vừa"
    elif amount < 50000000:
        return "Lớn"
    else:
        return "Rất lớn"

def display_table(data_list):
    """Hiển thị danh sách giao dịch dưới dạng bảng."""
    if not data_list:
        print("\n[Thông báo]: Danh sách giao dịch đang trống.")
        return
    
    print("\n" + "="*110)
    print(f"{'Mã TX':<10} | {'Nội dung':<25} | {'Loại':<6} | {'Số tiền gốc':<15} | {'Thuế':<6} | {'Thực tế':<15} | {'Quy mô'}")
    print("-"*110)
    for t in data_list:
        print(f"{t['id']:<10} | {t['desc']:<25} | {t['type']:<6} | {t['amount']:<15,.0f} | {t['tax']:<6}% | {t['final']:<15,.0f} | {t['scale']}")
    print("="*110)

def add_transaction():
    """Ghi nhận giao dịch mới."""
    print("\n--- Thêm giao dịch mới ---")
    tid = input("Nhập Mã TX: ").strip()
    if not tid or any(t['id'] == tid for t in transactions):
        print("[Lỗi]: Mã không được để trống hoặc bị trùng!")
        return

    desc = input("Nhập nội dung: ").strip()
    if not desc:
        print("[Lỗi]: Nội dung không được để trống!")
        return

    t_type = input("Loại giao dịch (Thu/Chi): ").capitalize()
    if t_type not in ["Thu", "Chi"]:
        print("[Lỗi]: Chỉ nhập 'Thu' hoặc 'Chi'!")
        return

    try:
        amount = float(input("Số tiền phát sinh: "))
        tax = float(input("Thuế suất (%): "))
        if amount <= 0 or tax < 0: raise ValueError
    except ValueError:
        print("[Lỗi]: Dữ liệu số không hợp lệ!")
        return

    final_amount = amount * (1 + tax / 100)
    transactions.append({
        'id': tid, 'desc': desc, 'type': t_type, 
        'amount': amount, 'tax': tax, 
        'final': final_amount, 'scale': classify_scale(final_amount)
    })
    print("[Thành công]: Đã thêm giao dịch!")

def update_transaction():
    """Cập nhật chứng từ."""
    tid = input("Nhập mã TX cần cập nhật: ")
    for t in transactions:
        if t['id'] == tid:
            print("Nhập thông tin mới (để trống để giữ nguyên):")
            t['desc'] = input(f"Nội dung [{t['desc']}]: ") or t['desc']
            t['type'] = input(f"Loại [{t['type']}]: ") or t['type']
            try:
                t['amount'] = float(input(f"Số tiền [{t['amount']}]: ") or t['amount'])
                t['tax'] = float(input(f"Thuế [{t['tax']}]: ") or t['tax'])
                t['final'] = t['amount'] * (1 + t['tax'] / 100)
                t['scale'] = classify_scale(t['final'])
                print("[Thành công]: Đã cập nhật!")
            except:
                print("[Lỗi]: Dữ liệu số không hợp lệ!")
            return
    print("[Lỗi]: Không tìm thấy mã giao dịch.")

def delete_transaction():
    """Xóa giao dịch."""
    tid = input("Nhập mã TX muốn xóa: ")
    for i, t in enumerate(transactions):
        if t['id'] == tid:
            confirm = input(f"Bạn có chắc muốn xóa {tid}? (Y/N): ")
            if confirm.upper() == 'Y':
                transactions.pop(i)
                print("[Thành công]: Đã xóa giao dịch.")
                return
            return
    print("[Lỗi]: Không tìm thấy mã giao dịch.")


while True:
        choice = input("""
========== QUẢN LÝ TÀI CHÍNH - DÒNG TIỀN ==========
1. Hiển thị nhật ký giao dịch
2. Ghi nhận giao dịch mới
3. Cập nhật chứng từ giao dịch
4. Xóa giao dịch lỗi
5. Tìm kiếm giao dịch
6. Thống kê tổng dòng tiền
8. Thoát chương trình
=====================================================
Mời chọn chức năng (0-8): """)
        
        match choice:
            case "1": display_table(transactions)
            case "2": add_transaction()
            case "3": update_transaction()
            case "4": delete_transaction()
            case "5": search_transaction()
            case "6": statistics()
            case "8":
                print("\nCảm ơn bạn đã sử dụng phần mềm! [Chương trình kết thúc]")
                break
            case _:
                print("\n[Lỗi]: Lựa chọn không hợp lệ, vui lòng chọn từ 0-6!")
