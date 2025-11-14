from fasthtml.common import *
import matplotlib.pyplot as plt

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE
from employee_events
import QueryBase, Employee, Team

# import the load_model function from the utils.py file
#### YOUR CODE HERE
from utils.py import load_model

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import (FormGroup, CombinedComponent)

# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE
class ReportDropdown(Dropdown):
    
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE  
    def build_component(self, entity_id, model):
    parent_data = super().build_component(entity_id, model)

        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE
        self.label = load_model.name
        
        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE
        return parent_data
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE
    def component_data(self, entity_id, model):
    parent_data = super().component_data(entity_id, model)

        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids
        #class EmployeeEvents:
            def __init__(self, model):
                self.model = model

            def employee_events(self):
                user_types = self.model.get_user_types()  # This should return a list of user types
                user_info = []

                for user in user_types:
                    user_info.append({
                        'name': user.name,  
                        'id': user.id       
                    })

                return user_info

# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE
class Header(BaseComponent):

    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE
    def build_component(self, entity_id, model):
    parent_data = super().build_component(entity_id, model)
        
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE
        def __init__(self, model):
        self.model = model

        def render_name(self):
            # Assuming the model has a 'name' attribute
            return H1(self.model.name)
          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE
class LineChart(MatplotlibViz):
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model):
    parent_data = super().visualization(entity_id, model)
    
        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        def __init__(self, model):
            self.model = model

        def get_event_data(self, asset_id):
            # Call the model's event_counts method with the asset_id
            x, y = self.model.visualization(asset_id)
            return x, y
        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        self.model.fillna(0)
        
        # User the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE
        self.model.set_index('x')
        
        # Sort the index
        #### YOUR CODE HERE
        self.model.sort_index(ascending=True)
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE
        y_cumulative = self.model.cumsum('y')
        self.model.drop(columns=['y'])
        self.model.rename(columns={'y_cumulative': 'y'})
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE
        new_columns = ['Positive', 'Negative']
        self.model.columns = new_columns

        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        #### YOUR CODE HERE
        fig, ax = plt.subplots()
        
        # call the .plot method for the
        # cumulative counts dataframe
        #### YOUR CODE HERE
        ax.plot(df['x'], df['Positive'], label='Series 1', color='blue')
        ax.plot(df['x'], df['Negative'], label='Series 2', color='orange')

        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        # Use keyword arguments to set 
        # the border color and font color to black. 
        # Reference the base_components/matplotlib_viz file 
        # to inspect the supported keyword arguments
        #### YOUR CODE HERE
        def set_axis_styling(self, ax, bordercolor='black', fontcolor='black'):    
            ax.title.set_color(fontcolor)
            ax.xaxis.label.set_color(fontcolor)
            ax.yaxis.label.set_color(fontcolor)
        
        # Set title and labels for x and y axis
        #### YOUR CODE HERE
        ax.set_xlabel('Event Date')
        ax.set_ylabel('Event Cumulative Counts')
        ax.set_title('Event Subplot')
        ax.legend()

# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE
class BarChart(MatplotlibViz):

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE
    class predictor:
    def __init__(self, model_path):
        # Create a predictor class attribute
        self.predictor = load_model(model_path)

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model):
    parent_data = super().visualization(entity_id, model)

        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE
        def __init__(self, model):
            self.model = model

        def get_asset_data(self, asset_id):
            # Pass the asset_id to the model's model_data method
            return self.model.model_data(asset_id)

        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE
        def __init__(self, model):
            self.predictor = Predictor(model)

        def get_probabilities(self, data):
            # Use the predictor class attribute to call predict_proba
            probabilities = self.predictor.predict_proba(data)
            return probabilities

        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE
        probabilities.set_index(:,1)
        
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        pred = probabilities

        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE

        if name = 'team':
             return mean(probabilities)
            
        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE
        else:
            return probabilities.iloc[0]
        
        # Initialize a matplotlib subplot
        #### YOUR CODE HERE
        fig, ax = plt.subplots()
        
        # Run the following code unchanged
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE
        def set_axis_styling(self, ax, bordercolor='black', fontcolor='black'):    
            ax.title.set_color(fontcolor)
            ax.xaxis.label.set_color(fontcolor)
            ax.yaxis.label.set_color(fontcolor)
 
# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
#### YOUR CODE HERE
class Visualizations(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    #### YOUR CODE HERE
    children = []
    def __init__(self):
        # Initialize instances of LineChart and BarChart
        self.children = [LineChart(), BarChart()]

    #def show_charts(self):
    #    for chart in self.children:
    #        print(chart.display())

    # Leave this line unchanged
    outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE
class NotesTable(DataTable):

    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE
    def component_data(self, entity_id, model):
    parent_data = super().component_data(entity_id, model)
        
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE
        def __init__(self, model):
            self.model = model

        def get_asset_data(self, entity_id):
            return self.model.notes(entity_id)

    
class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR CODE HERE
class Report(CombinedComponents):

    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    #### YOUR CODE HERE
    children = []
    def __init__(self):
        self.children = [Header(), DashboardFilters(), Visualizations(), NotesTable()]


# Initialize a fasthtml app 
#### YOUR CODE HERE
app, route = fast_app()

# Initialize the `Report` class
#### YOUR CODE HERE
class Report:
    def __init__(self, title, content):
        self.title = title  # Title of the report
        self.content = content  # Content of the report

    def display_report(self):
        # Method to display the report
        print(f"Report Title: {self.title}")
        print("Content:")
        print(self.content)

    # Example usage
    #report_title = "Monthly Sales Report"
    #report_content = "This report contains the sales data for the month of January."

    # Initialize the Report class
    my_report = Report(report_title, report_content)

# Create a route for a get request
# Set the route's path to the root
#### YOUR CODE HERE
@route('/')
def get():

    # Call the initialized report
    # pass the integer 1 and an instance
    # of the Employee class as arguments
    # Return the result
    #### YOUR CODE HERE
    result = my_report.generate_report(1, Employee)
    raw_html = result/to_html()
    table = NotStr(raw_html)

# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
#### YOUR CODE HERE
@route('/employee/{Employee}')
def get(Employee:str='')

    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    result = my_report.generate_report(1, Employee)
    raw_html = result/to_html()
    table = NotStr(raw_html)
    frame = df[df.employee.str.contains(Employee)]

    if employee:
        frame = frame[frame.employee == employee]

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
#### YOUR CODE HERE
@route('/team/{Team}')
def get(Team:str='')

    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    result = my_report.generate_report(1, Employee)
    raw_html = result/to_html()
    table = NotStr(raw_html)
    frame = df[df.team.str.contains(Team)]

    if team:
        frame = frame[frame.team == team]


# Keep the below code unchanged!
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    


serve()
