import sys 
from src.my_own_project.logger import logging
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)
console = Console()

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno

    

     # 🎨 Rich formatted panel
    error_message = Panel.fit(
        f"[bold red]Error Occurred[/bold red]\n\n"
        f"[yellow]📂 File:[/yellow] {file_name}\n"
        f"[cyan]📍 Line:[/cyan] {line_number}\n"
        f"[green]💬 Message:[/green] {str(error)}",
        title="[bold red]Exception[/bold red]",
        border_style="red"
    )


    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)
    
    def __str__(self):
        # Print colored panel in console
        console.print(self.error_message)
        return self.error_message