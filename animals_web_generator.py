import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding='utf-8') as handle:
      return json.load(handle)


def serialize_animal(animal_obj):
    """Returns an HTML list item (<li>) containing formatted information about a single animal."""
    output = ''
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>  {animal_obj['name']}</div>"
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>"
    output += f"<strong>Location</strong>: {animal_obj['locations'][0]}<br/>"
    if 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>"
    output += '</p>'
    output += '</li>'

    return output


def generate_animals_html(output):
    """Generates an HTML file by inserting animal data into a template and adding UTF-8 metadata."""
    with open("animals_template.html", "r", encoding="utf-8") as f:
        html_template = f.read()
        html_template = html_template.replace(
        "<head>",
        "<head>\n    <meta charset=\"UTF-8\">"
        )

    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(html_output)


def main():
    data = load_data("animals_data.json")

    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)

    generate_animals_html(output)


if __name__ == "__main__":
    main()

