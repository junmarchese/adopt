from flask import Flask, render_template, redirect, url_for, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adoptgoldendoodlepuppy'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    connect_db(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()


@app.route('/')
def list_pets():
    """Retrieve and display list of all pets."""
    pets = Pet.query.all()
    return render_template('pet_list_homepage.html', pets=pets)

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""
    
    return render_template('404.html'), 404

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Create a new pet."""
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))
    
    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def display_edit_pet(pet_id):
    """Display a pet's details and show a form that allows user to edit pet details."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))
    
    return render_template('pet_detail_or_edit.html', pet=pet, form=form)


if __name__ == '__main__':
    app.run(debug=True)






