import os
import sys
import time
import random

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.layout import Layout
from rich.live import Live
from rich.text import Text

console = Console()

# Theme palettes (Rich color strings)
THEMES = {
    "green": {"primary": "bright_green", "dim": "green", "alert": "bright_red"},
    "amber": {"primary": "bright_yellow", "dim": "yellow", "alert": "bright_red"},
    "cyan": {"primary": "bright_cyan", "dim": "cyan", "alert": "bright_magenta"},
    "red": {"primary": "bright_red", "dim": "red", "alert": "bright_yellow"},
}

current_theme = "green"

ASCII_BANNER = r"""
 ██████╗ ███████╗██████╗  ██████╗ ████████╗███████╗██████╗ ███╗   ███╗
██╔════╝ ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║  ███╗█████╗  ██████╔╝██║   ██║   ██║   █████╗  ██████╔╝██╔████╔██║
██║   ██║██╔══╝  ██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
╚██████╔╝███████╗██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
 ╚═════╝ ╚══════╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
"""


def beep():
    """Trigger terminal system bell if supported."""
    sys.stdout.write("\a")
    sys.stdout.flush()


def typewrite(text: str, delay: float = 0.015, style: str = None):
    """Simulate authentic typewriter output with audio-tactile feedback."""
    for char in text:
        console.print(char, end="", style=style or THEMES[current_theme]["primary"])
        time.sleep(delay)
    console.print()


def show_banner():
    color = THEMES[current_theme]["primary"]
    console.print(Panel(
        Text(ASCII_BANNER, justify="center", style=color),
        title="[bold]GEBOTERM // KERNEL v4.09.2[/bold]",
        subtitle="[bold]ROOT ACCESS ACTIVE // HOST: LOCALHOST[/bold]",
        border_style=color,
        padding=(0, 2)
    ))
    console.print(f"Type [bold]{THEMES[current_theme]['primary']}help[/] to inspect available subroutines.\n")


def cmd_matrix(duration: float = 4.0):
    """Visualizes an active memory/packet stream."""
    typewrite("Initializing kernel data stream...", delay=0.01)
    time.sleep(0.3)
    
    chars = "0123456789ABCDEF!@#$%^&*<>~+="
    end_time = time.time() + duration
    
    with Live(console=console, screen=False, refresh_per_second=20) as live:
        while time.time() < end_time:
            line = "".join(random.choice(chars) + " " for _ in range(35))
            styled_line = Text(line, style=THEMES[current_theme]["primary"])
            live.update(styled_line)
            time.sleep(0.04)
            
    console.print(f"[{THEMES[current_theme]['dim']}]Stream terminated. Buffer cleared.[/]\n")


def cmd_scan():
    """Scan local node segments for vulnerable entry points."""
    color = THEMES[current_theme]["primary"]
    dim_color = THEMES[current_theme]["dim"]
    
    typewrite("Deploying network pulse across subnet 192.168.1.0/24...", delay=0.01)
    time.sleep(0.5)

    table = Table(title="ACTIVE NODES DETECTED", border_style=dim_color, header_style=f"bold {color}")
    table.add_column("NODE IP", justify="left")
    table.add_column("PORT", justify="center")
    table.add_column("STATUS", justify="center")
    table.add_column("TARGET SERVICE", justify="left")

    nodes = [
        ("192.168.1.14", "8000", "[bright_green]OPEN[/]", "FastAPI Microservice (StudyTracker)"),
        ("192.168.1.42", "5432", "[bright_yellow]FILTERED[/]", "PostgreSQL Main Relational DB"),
        ("192.168.1.88", "22", "[bright_red]CRITICAL[/]", "OpenSSH 7.2p1 (CVE-2016-6210)"),
        ("192.168.1.103", "3306", "[bright_green]OPEN[/]", "MySQL Expenses Core"),
    ]

    for ip, port, status, service in nodes:
        table.add_row(ip, port, status, service)
        time.sleep(0.15)

    console.print(table)
    console.print()


def cmd_breach(target: str = "192.168.1.88"):
    """Execute dynamic injection protocol with animated progress."""
    color = THEMES[current_theme]["primary"]
    dim_color = THEMES[current_theme]["dim"]
    
    typewrite(f"Initiating injection exploit against target {target}...", delay=0.02)
    beep()

    steps = [
        ("Bypassing firewall ingress filters", 1.2),
        ("Flooding memory address registers", 1.8),
        ("Injecting shellcode payload", 1.4),
        ("Escalating permissions to UID 0 (root)", 1.0),
    ]

    with Progress(
        SpinnerColumn(style=color),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(complete_style=color, finished_style="bold green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(f"[{color}]Breach Protocol", total=100)
        chunk = 100 / len(steps)
        
        for desc, wait in steps:
            progress.update(task, description=f"[{color}]{desc}...")
            time.sleep(wait)
            progress.advance(task, chunk)
            beep()

    console.print(f"[bold bright_green]ACCESS GRANTED[/bold bright_green] -> Shell established at [{color}]{target}:/root#[/]\n")


def cmd_decrypt():
    """Interactive timing challenge to lock memory registers."""
    color = THEMES[current_theme]["primary"]
    typewrite("MEMLOCK DECRYPT ENGAGED.", delay=0.02)
    typewrite("Watch the rotating hex hash. When the target key aligns, press ENTER to lock it in.", delay=0.01)
    
    target_hex = "0x7F"
    time.sleep(0.5)
    console.print(f"\nTARGET REGISTER: [bold {color}]{target_hex}[/]\n")
    
    for round_idx in range(1, 4):
        time.sleep(0.5)
        matched = False
        console.print(f"Cycle {round_idx}/3: Press Enter when [bold]{target_hex}[/] is displayed!")
        
        # Fast rotating display
        pool = ["0x1A", "0x3F", "0x5E", target_hex, "0x9C", "0xAA", "0xBF"]
        random.shuffle(pool)
        
        # Simple interactive trigger
        for item in pool:
            sys.stdout.write(f"\r  HOLDING: [{item}] ")
            sys.stdout.flush()
            time.sleep(0.35)
            
        console.print()
        choice = input("  Lock register value: ").strip().upper()
        
        if choice == target_hex:
            beep()
            console.print(f"  [bold bright_green]✓ LOCKED SEGMENT {round_idx}[/]\n")
        else:
            console.print(f"  [bold bright_red]✗ DECRYPTION FAILED. Desynchronized register.[/]\n")
            return

    console.print(f"[bold bright_green]ALL 3 SEGMENTS LOCKED. ACCESS KEY: 994-SHADOW-OVERRIDE[/bold bright_green]\n")


def cmd_theme(arg: str):
    global current_theme
    theme_name = arg.lower().strip()
    if theme_name in THEMES:
        current_theme = theme_name
        console.print(f"Palette updated to [{THEMES[current_theme]['primary']}]{theme_name.upper()}[/].\n")
    else:
        available = ", ".join(THEMES.keys())
        console.print(f"Unknown theme. Choose from: {available}\n", style=THEMES[current_theme]["alert"])


def cmd_cat(filename: str):
    color = THEMES[current_theme]["primary"]
    dim_color = THEMES[current_theme]["dim"]
    
    files = {
        "manifesto.txt": (
            "We build inside the shell, carving utility from raw silicon.\n"
            "State is an illusion; memory is temporary; uptime is everything."
        ),
        "notes.txt": (
            "TODO:\n"
            "- Optimize FastAPI async session pools.\n"
            "- Inspect open port 22 vulnerabilities.\n"
            "- Keep the CRT phosphor bright."
        )
    }

    if filename in files:
        console.print(Panel(files[filename], title=filename, border_style=dim_color, style=color))
    else:
        console.print(f"cat: {filename}: No such file or directory.", style=THEMES[current_theme]["alert"])
    console.print()


def show_help():
    color = THEMES[current_theme]["primary"]
    dim_color = THEMES[current_theme]["dim"]
    
    commands = [
        ("scan", "Probe local network nodes and inspect vulnerable ports"),
        ("breach <target>", "Run automated injection assault against a host"),
        ("decrypt", "Play interactive memory alignment mini-game"),
        ("matrix", "Stream high-frequency raw bytecode onto stdout"),
        ("theme <name>", "Switch palette: green | amber | cyan | red"),
        ("cat <file>", "Inspect file: manifesto.txt | notes.txt"),
        ("clear", "Flush the terminal screen buffer"),
        ("exit", "Terminate active session"),
    ]

    table = Table(title="AVAILABLE KERNEL COMMANDS", border_style=dim_color, header_style=f"bold {color}")
    table.add_column("COMMAND", style=f"bold {color}")
    table.add_column("DESCRIPTION", style=dim_color)

    for cmd, desc in commands:
        table.add_row(cmd, desc)

    console.print(table)
    console.print()


def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_banner()

    while True:
        try:
            color = THEMES[current_theme]["primary"]
            prompt_str = f"root@cyber-node:~# "
            user_input = console.input(f"[bold {color}]{prompt_str}[/]").strip()
            
            if not user_input:
                continue

            parts = user_input.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            if cmd in ("exit", "quit"):
                typewrite("Terminating socket connection. Good hunting...", delay=0.02)
                break
            elif cmd == "clear":
                os.system("cls" if os.name == "nt" else "clear")
                show_banner()
            elif cmd == "help":
                show_help()
            elif cmd == "scan":
                cmd_scan()
            elif cmd == "breach":
                target = arg if arg else "192.168.1.88"
                cmd_breach(target)
            elif cmd == "matrix":
                cmd_matrix()
            elif cmd == "decrypt":
                cmd_decrypt()
            elif cmd == "theme":
                cmd_theme(arg)
            elif cmd == "cat":
                cmd_cat(arg)
            else:
                console.print(f"Command not recognized: '{cmd}'. Enter 'help' for options.\n", style=THEMES[current_theme]["alert"])

        except KeyboardInterrupt:
            console.print("\nSession interrupted. Exiting...")
            break


if __name__ == "__main__":
    main()