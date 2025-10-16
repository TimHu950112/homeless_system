from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  無家者服務整合平台")
    print("="*60)
    print("\n✓ 系統啟動中...")
    print("✓ 使用 JSON 本地數據存儲")
    print("✓ 數據文件位置: data/")
    print("\n測試帳號：")
    print("  一般用戶: user1 / password123 (100點)")
    print("  一般用戶: user2 / password123 (50點)")
    print("  社工: social_worker / password123")
    print("  管理員: admin / admin123")
    print("\n訪問網址: http://localhost:5000")
    print("="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5500)
