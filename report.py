def generate_report(results, format="txt"):
    if format == "txt":
        with open("report.txt", "w") as file:
            for result in results:
                file.write(result + "\n")
    elif format == "html":
        with open("report.html", "w") as file:
            file.write("<html><body><h1>pentest report</h1>")
            for result in results:
                file.write(f"<p>{result}</p>")
            file.write("</body></html>")