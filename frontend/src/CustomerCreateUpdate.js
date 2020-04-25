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
        // window.alert("componentDidMount")
        if (params && params.pk) {
            window.alert("componentDidMount - if")
            customersService.getCustomer(params.pk).then((c)=> {
                // this.refs.firstName.value = c.first_name;
                // this.refs.lastName.value = c.last_name;
                // this.refs.email.value = c.email;
                // this.refs.phone.value = c.phone;
                // this.refs.address.value = c.address;
                // this.refs.description.value = c.description;

                this.firstName = c.first_name;
                this.lastName = c.last_name;
                this.email = c.email;
                this.phone = c.phone;
                this.address = c.address;
                this.description = c.description;

                // this.setFirstName(c);
                // this.setLastName(c);
                // this.setEmail(c);
                // this.setPhone(c);
                // this.setAddress(c);
                // this.setDescription(c);
            })
        }
    }

    handleCreate() {
        // window.alert("handleCreate")
        // this.setFirstName();
        // this.setLastName();
        // this.setEmail();
        // this.setPhone();
        // this.setAddress();
        // this.setDescription();
        customersService.createCustomer({
            // "first_name": this.refs.firstName.value,
            // "last_name": this.refs.lastName.value,
            // "email": this.refs.email.value,
            // "phone": this.refs.phone.value,
            // "address": this.refs.address.value,
            // "description": this.refs.description.value

            // "first_name": this.firstName,
            // "last_name": this.lastName,
            // "email": this.email,
            // "phone": this.phone,
            // "address": this.address,
            // "description": this.description

            "first_name": this.refFirstName.current.value,
            "last_name": this.refLastName.current.value,
            "email": this.refEmail.current.value,
            "phone": this.refPhone.current.value,
            "address": this.refAddress.current.value,
            "description": this.refDescription.current.value
        }).then((result)=> {
            window.alert("Customer created!");
        }).catch(()=> {
            window.alert("There was an error! Please re-check your form.");
        });
    }
    handleUpdate(pk) {
        customersService.updateCustomer({
            "pk": pk,
            // "first_name": this.refs.firstName.value,
            // "last_name": this.refs.lastName.value,
            // "email": this.refs.email.value,
            // "phone": this.refs.phone.value,
            // "address": this.refs.address.value,
            // "description": this.refs.description.value

            "first_name": this.firstName,
            "last_name": this.lastName,
            "email": this.email,
            "phone": this.phone,
            "address": this.address,
            "description": this.description
        }).then((result)=> {
            alert("Customer updated!");
        }).catch(()=> {
            alert("There was an error! Please re-check your form.");
        })
    }
    handleSubmit(event) {
        // window.alert("handleSubmit")
        const {match: { params } } = this.props;
        if (params && params.pk) {
            // window.alert("handleUpdate")
            this.handleUpdate(params.pk);
        }
        else {
            this.handleCreate();
        }
        event.preventDefault();
    }


    // setFirstName = element => {
    //     window.alert(element)
    //     this.firstName = element;
    //     window.alert(this.firstName)
    // };
    // setLastName = element => {
    //     this.lastName = element;
    // };
    // setEmail = element => {
    //     this.email = element;
    // };
    // setPhone = element => {
    //     this.phone = element;
    // };
    // setAddress = element => {
    //     this.address = element;
    // };
    // setDescription = element => {
    //     this.description = element;
    // };


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
    // render() {
    //     return (
    //       <form onSubmit={this.handleSubmit}>
    //           <div className="form-group">
    //               <label>First Name: </label>
    //               <input className="form-control" type="text" ref={this.setFirstName} />
    //
    //               <label>Last Name: </label>
    //               <input className="form-control" type="text" ref={this.setLastName} />
    //
    //               <label>Email: </label>
    //               <input className="form-control" type="text" ref={this.setEmail} />
    //
    //               <label>Phone: </label>
    //               <input className="form-control" type="text" ref={this.setPhone} />
    //
    //               <label>Address: </label>
    //               <input className="form-control" type="text" ref={this.setAddress} />
    //
    //               <label>Description: </label>
    //               <textarea className="form-control" ref={this.setDescription}></textarea>
    //
    //               <input className="btn btn-primary" type="submit" value="Submit" />
    //           </div>
    //       </form>
    //     );
    // render() {
    //     return (
    //       <form onSubmit={this.handleSubmit}>
    //           <div className="form-group">
    //               <label>First Name: </label>
    //               <input className="form-control" type="text" ref="first_name" />
    //
    //               <label>Last Name: </label>
    //               <input className="form-control" type="text" ref="last_name" />
    //
    //               <label>Email: </label>
    //               <input className="form-control" type="text" ref="email" />
    //
    //               <label>Phone: </label>
    //               <input className="form-control" type="text" ref="phone" />
    //
    //               <label>Address: </label>
    //               <input className="form-control" type="text" ref="address" />
    //
    //               <label>Description: </label>
    //               <textarea className="form-control" ref="description"></textarea>
    //
    //               <input className="btn btn-primary" type="submit" value="Submit" />
    //           </div>
    //       </form>
    //     );
    }
}
export default CustomerCreateUpdate;