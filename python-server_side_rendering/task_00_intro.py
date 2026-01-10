import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    Files are named output_X.txt starting from 1.
    """

    # ---------- Validate input types ----------
    if not isinstance(template, str):
        print("Error: Invalid template type. Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid attendees type. Attendees must be a list of dictionaries.")
        return

    # ---------- Handle empty inputs ----------
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------- Process each attendee ----------
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"

        # ---------- Write output file ----------
        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
