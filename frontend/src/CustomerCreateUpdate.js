import React, { Component } from "react";
import CustomersService from "./CustomersService";

const customersService = new CustomersService();

class CustomerCreateUpdate extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);

        this.refFirstName = React.createRef();
        this.refLastName = React.createRef();
        this.refEmail = React.createRef();
        this.refPhone = React.createRef();
        this.refAddress = React.createRef();
        this.refDescription = React.createRef();
    }

    componentDidMount() {
        const {match: { params } } = this.props;
        if (params && params.pk) {
            customersService.getCustomer(params.pk).then((c)=> {
                this.refFirstName.current.value = c.first_name;
                this.refLastName.current.value = c.last_name;
                this.refEmail.current.value = c.email;
                this.refPhone.current.value = c.phone;
                this.refAddress.current.value = c.address;
                this.refDescription.current.value = c.description;
            })
        }
    }

    handleCreate() {
        customersService.createCustomer({
            "first_name": this.refFirstName.current.value,
            "last_name": this.refLastName.current.value,
            "email": this.refEmail.current.value,
            "phone": this.refPhone.current.value,
            "address": this.refAddress.current.value,
            "description": this.refDescription.current.value
        }).then((result)=> {
            alert("Customer created!");
        }).catch(()=> {
            alert("There was an error! Please re-check your form.");
        });
    }
    handleUpdate(pk) {
        customersService.updateCustomer({
            "pk": pk,
            "first_name": this.refFirstName.current.value,
            "last_name": this.refLastName.current.value,
            "email": this.refEmail.current.value,
            "phone": this.refPhone.current.value,
            "address": this.refAddress.current.value,
            "description": this.refDescription.current.value
        }).then((result)=> {
            alert("Customer updated!");
        }).catch(()=> {
            alert("There was an error! Please re-check your form.");
        })
    }
    handleSubmit(event) {
        const {match: { params } } = this.props;
        if (params && params.pk) {
            this.handleUpdate(params.pk);
        }
        else {
            this.handleCreate();
        }
        event.preventDefault();
    }

    render() {
        return (
          <form onSubmit={this.handleSubmit}>
              <div className="form-group">
                  <label>First Name: </label>
                  <input className="form-control" type="text" ref={this.refFirstName} />

                  <label>Last Name: </label>
                  <input className="form-control" type="text" ref={this.refLastName} />

                  <label>Email: </label>
                  <input className="form-control" type="text" ref={this.refEmail} />

                  <label>Phone: </label>
                  <input className="form-control" type="text" ref={this.refPhone} />

                  <label>Address: </label>
                  <input className="form-control" type="text" ref={this.refAddress} />

                  <label>Description: </label>
                  <textarea className="form-control" ref={this.refDescription}></textarea>

                  <input className="btn btn-primary" type="submit" value="Submit" />
              </div>
          </form>
        );
    }
}
export default CustomerCreateUpdate;
