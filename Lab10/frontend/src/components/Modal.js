import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
} from "reactstrap";

export default class CustomModal extends Component {
    constructor(props) {
    super(props);
    this.state = {
        activeItem: this.props.activeItem
    };
    }
    handleChange = e => {
    let { name, value } = e.target;
    if (e.target.type === "checkbox") {
        value = e.target.checked;
    }
    const activeItem = { ...this.state.activeItem, [name]: value };
    this.setState({ activeItem });
    };
    render() {
    const { toggle, onSave } = this.props;
    return (
        <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>What to do?</ModalHeader>
        <ModalBody>
            <Form>
            <FormGroup>
                <Label for="title">Title</Label>
                <Input
                type="text"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="What should I do?"
                />
            </FormGroup>
            <FormGroup>
                <Label for="description">Description</Label>
                <Input
                type="text"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter description of the task."
                />
            </FormGroup>
            <FormGroup>
                <Label for="title">Notes</Label>
                <Input
                type="text"
                name="notes"
                value={this.state.activeItem.notes}
                onChange={this.handleChange}
                placeholder="What should I remember specifically?"
                />
            </FormGroup>
            <FormGroup check>
                <Label for="finished">
                <Input
                    type="checkbox"
                    name="finished"
                    checked={this.state.activeItem.finished}
                    onChange={this.handleChange}
                />
                Finished
                </Label>
            </FormGroup>
            <FormGroup>
                <Label for="date">
                <Input
                    type="date"
                    name="date"
                    checked={this.state.activeItem.date}
                    onChange={this.handleChange}
                />
                </Label>
            </FormGroup>

            </Form>
        </ModalBody>
        <ModalFooter>
            <Button color="success" onClick={() => onSave(this.state.activeItem)}>
            Save
            </Button>
        </ModalFooter>
        </Modal>
    );
    }
}