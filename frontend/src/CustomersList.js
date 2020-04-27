import React, { Component } from "react";
import CustomersService from "./CustomersService";

const customersService = new CustomersService();

class CustomersList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            customers: [],
            prevPageURL: '',
            nextPageURL: '',
        };
        this.prevPage = this.prevPage.bind(this);
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    componentDidMount() {
        var self = this;
        customersService.getCustomers().then(function (result) {
            console.log(" prev = ", result.prevlink);
            console.log(" next = ", result.nextlink);
            self.setState({customers: result.data, prevPageURL: result.prevlink})
            self.setState({customers: result.data, nextPageURL: result.nextlink})
        });
    }

    handleDelete(e, pk){
        var self = this;
        customersService.deleteCustomer({pk: pk}).then(()=>{
            var newArr = self.state.customers.filter(function (obj) {
                return obj.pk !== pk;
            });

            self.setState({customer: newArr})
        });
    }
    prevPage(){
        var self = this;
        console.log(this.state.prevPageURL);
        customersService.getCustomersByURL(this.state.prevPageURL).then((result)=>{
            console.log("*prev = ", result.prevlink);
            console.log(" next = ", result.nextlink);
            self.setState({
                customers: result.data,
                prevPageURL: result.prevlink,
                nextPageURL: result.nextlink,
            })
        });
    }
    nextPage(){
        var self = this;
        console.log(this.state.nextPageURL);
        customersService.getCustomersByURL(this.state.nextPageURL).then((result)=>{
            console.log(" prev = ", result.prevlink);
            console.log("*next = ", result.nextlink);
            self.setState({
                customers: result.data,
                prevPageURL: result.prevlink,
                nextPageURL: result.nextlink,
            })
        });
    }

    render() {
        return (
            <div className="customers--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>#</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Address</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.customers.map( c =>
                        <tr key={c.pk}>
                            <td>{c.pk}</td>
                            <td>{c.first_name}</td>
                            <td>{c.last_name}</td>
                            <td>{c.email}</td>
                            <td>{c.phone}</td>
                            <td>{c.address}</td>
                            <td>{c.description}</td>
                            <td>
                                <button onClick={(e)=> this.handleDelete(e, c.pk)}>Delete</button>
                                <a href={"/customer/" + c.pk}>Update</a>
                            </td>
                        </tr>
                    )}
                    </tbody>
                </table>
                <button className="btn btn-primary mr-2" onClick={ this.prevPage }>Prev</button>
                <button className="btn btn-primary mr-2" onClick={ this.nextPage }>Next</button>
            </div>
        );
    }
}
export default CustomersList;
