import flet as ft


def main(page: ft.Page):

    def home_view():
        return ft.View(
            route='/',
            bgcolor = ft.Colors.BLUE_800,
            controls=[
                ft.Text('Home'),
                ft.Row(
                    [
                        ft.TextButton("Lists",on_click=lambda e: page.go("/lists")),
                        ft.TextButton("Settings")
                    ]
                )
            ]
        )
    def lists_view():
        return ft.View(
            route='/lists',
            controls=[
                ft.Text('Lists'),
                ft.Row(
                    [
                        ft.TextButton("⬅️Home", on_click=lambda e: page.go("/")),
                        ft.TextButton("Create a list", on_click=lambda e: open_dialog("create_list")),
                        ft.TextButton("Add a word", on_click=lambda e: page.go("/add_word"))
                    ]
                )
            ]
        )

    def add_word_view():
        return ft.View(
            route='/add_word',
            controls=[
                ft.Text('Add word'),
                ft.Row(
                    [
                        ft.TextButton("⬅️Home", on_click=lambda e: page.go("/")),
                        ft.TextButton("Add a word")
                    ]
                )
            ]
        )

    def open_dialog(dialog_type):
        if dialog_type == 'create_list':
            list_name = ft.TextField(label="List name")
            dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Create a list"),
                content=list_name,
                actions=[
                    ft.TextButton("Cancel", on_click=lambda e: close_dialog(dialog)),
                    ft.TextButton("Create", on_click=lambda e: create_list(list_name.value,dialog)),
                ],
            )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    def create_list(list_name, dialog):
        print(f"{list_name} was created!")

    routes = {
        "/": home_view,
        "/lists": lists_view,
        "/add_word": add_word_view
    }

    # --- Router ---
    def route_change(e):
        page.views.clear()

        view_builder = routes.get(page.route)

        if view_builder:
            page.views.append(view_builder())

        page.update()

    page.on_route_change = route_change

    page.window.width = 600
    page.window.height = 700
    page.window.center()
    page.update()

    route_change(None)

ft.run(main)
