# credit_card
Credit card number validator

## Usage local
1. Clone this project.
2. Create a Postgres database.
3. Configure your `.env`. Follow `example.env`.
4. Install the requirements.
5. Run the migrations.

_Important: this project uses Python 3.6._

## Running tests
Run `pytest`.

## Use the app
1. Access http://creditcardvalidator.herokuapp.com/
2. Create a `.txt` file with cards numbers, example:
```
8
4764090812631883
8764090812631882
698w736301999912
4444428018308048
0174-1178-7266-9253
5174-1178-7266-9253
576409283990812631883
5019298310297746
```
3. Upload the file and click on 'Upload' button
