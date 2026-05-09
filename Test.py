from pydoc import text

import flet as ft


def main(page: ft.Page):
    def home_view():
        return ft.View(
            route='/',
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
                        ft.TextButton("Create a list", on_click=open_dialog),
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

    def open_dialog(e):
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create a list"),
            content=ft.TextField(label="List name"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: close_dialog(dialog)),
                ft.TextButton("Create", on_click=lambda e: close_dialog(dialog)),
            ],
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

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

    route_change(None)

ft.run(main)
