import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
        try:
            peso=float(txtPeso.value.strip())
            altura=float(txtAltura.value.strip())
            imc=peso/(altura*altura)
            lblIMC.value=f"Tu IMC es de: {imc:.2f}"
            page.update()
            
        #Funcion para cerrar el cuadro de dialogo
            def cerrar_dialogo(e):
                page.dialog.open = False
                page.updape()
            # calcula el peso  del IMC
            if imc<18.5:
                dialog=ft.AlertDialog(
                    title=ft.Text("resultado de imc"),
                    content=ft.Text("acualmente estas bajo de peso"),
                    actions=[ft.Text("ok",on_click=cerrar_duialog)],
                )
            elif 18.5 <= imc <24.9:
                dialog=ft.AlertDialog(
                    title=ft.Text("resultado de imc"),
                    content=ft.Text("tu peso es normal"),
                    actions=[ft.Text("ok",on_click=cerrar_duialog)],
                    
                )
            elif 25 <= imc <30:
                dialog=ft.AlertDialog(
                        title=ft.Text("resultado de imc"),
                        content=ft.Text("tienes sobrepeso"),
                        actions=[ft.Text("ok",on_click=cerrar_duialog)],
                    )
            else:
                    dialog=ft.AlertDialog(
                        title=ft.Text("resultado de imc"),
                        content=ft.Text("tienes obesidad"),
                        actions=[ft.Text("ok",on_click=cerrar_duialog)],
                    )      
            page.dialog=dialog
            page.dialog.open = True
            page.update()
                
        except ValueError:
            def cerrar_dialog(e):
                page.dialog.open = False
                page.update()
                
                dialog=ft.AlertDialog(
                        title=ft.Text("Error"),
                        content=ft.Text("debes de ingresar valores numericos"),
                        actions=ft.TextButton[ft.TextButton("ok",on_click=cerrar_dialog)],
                        
                    )
                    
        page.dialog=dialog
        page.dialog.open= True
        page.update()

def main(page: ft.Page):
        page.title = "Calculadora de IMC" 
        page.bgcolor="PURPLE"
    
        txtPeso=ft.TextField(label="Ingresa tu peso")
        txtAltura=ft.TextField(label="Ingresa tu altura")
        lblIMC=ft.Text("Tu IMC es de: ")
    
        img=ft.Image(
            src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN
        )
        def on_cacular_click(e):
            calcular_imc(txtPeso,txtAltura,lblIMC,page)
    
    
        def limpiar(e):
            txtPeso.value=""
            txtAltura.value=""
            lblIMC.value="tu imc es:"
            page.update()
        
        btnCalcular=ft.ElevatedButton(text="Calculadora")
        btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
        page.add(
            
            ft.Column(
            controls=[
                txtPeso,
                txtAltura,
                lblIMC
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,
                btnLimpiar
            ],alignment="CENTER")
    )
        
    
    


ft.app(target=main,view=ft.AppView.WEB_BROWSER)