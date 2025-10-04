import customtkinter as ctk

def create_page1(app):

    page = ctk.CTkFrame(app)

    ctk.CTkLabel(page, text="Страница 1", font=("Arial", 20)).pack(pady=20)
    ctk.CTkButton(page, text="Вперед →", command=lambda: [page.pack_forget(), page2.pack(fill="both", expand=True)]).pack(pady=10)
    
    return page

def create_page2(app):

    page = ctk.CTkFrame(app)

    ctk.CTkLabel(page, text="Страница 2", font=("Arial", 20)).pack(pady=20)
    ctk.CTkButton(page, text="Вперед →", command=lambda: [page.pack_forget(), page3.pack(fill="both", expand=True)]).pack(pady=10)
    
    return page

def create_page3(app):

    page = ctk.CTkFrame(app)
    
    ctk.CTkLabel(page, text="Страница 3", font=("Arial", 20)).pack(pady=20)
    ctk.CTkButton(page, text="Вперед →", command=lambda: [page.pack_forget(), page1.pack(fill="both", expand=True)]).pack(pady=10)
    
    return page

def main():
    global page1, page2, page3
    
    app = ctk.CTk()
    app.geometry("900x700")
    app.resizable(False, False)
    

    page1 = create_page1(app)
    page2 = create_page2(app)
    page3 = create_page3(app)
    
    page1.pack(fill="both", expand=True)
    
    app.mainloop()

main()