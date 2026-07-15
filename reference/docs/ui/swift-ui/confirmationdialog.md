---
title: "ConfirmationDialog"
description: "A SwiftUI ConfirmationDialog component for presenting confirmation prompts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/confirmationdialog.md"
scraped_at: "2026-07-15T08:59:19.821589"
---

---
title: ConfirmationDialog
description: A SwiftUI ConfirmationDialog component for presenting confirmation prompts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ConfirmationDialog

A SwiftUI ConfirmationDialog component for presenting confirmation prompts.
iOS, tvOS, Included in Expo Go

Expo UI ConfirmationDialog matches the official SwiftUI [confirmationDialog API](https://developer.apple.com/documentation/swiftui/view/confirmationdialog\(_:ispresented:titlevisibility:actions:message:\)) and presents an action sheet-style dialog with a title, actions, and an optional message.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic confirmation dialog

Use `ConfirmationDialog.Trigger` to define the visible element and `ConfirmationDialog.Actions` to provide the dialog buttons.

```tsx
import { useState } from 'react';
import { Host, ConfirmationDialog, Button, Text } from '@expo/ui/swift-ui';

export default function BasicConfirmationDialogExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <ConfirmationDialog
        title="Are you sure?"
        isPresented={isPresented}
        onIsPresentedChange={setIsPresented}
        titleVisibility="visible">
        <ConfirmationDialog.Trigger>
          <Button label="Show Dialog" onPress={() => setIsPresented(true)} />
        </ConfirmationDialog.Trigger>
        <ConfirmationDialog.Actions>
          <Button label="Confirm" onPress={() => setIsPresented(false)} />
          <Button label="Cancel" role="cancel" />
        </ConfirmationDialog.Actions>
      </ConfirmationDialog>
    </Host>
  );
}
```

### Destructive action confirmation

Use `role="destructive"` on a `Button` inside `ConfirmationDialog.Actions` to style it as a destructive action.

```tsx
import { useState } from 'react';
import { Host, ConfirmationDialog, Button, Text } from '@expo/ui/swift-ui';

export default function DestructiveConfirmationDialogExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <ConfirmationDialog
        title="Delete Item?"
        isPresented={isPresented}
        onIsPresentedChange={setIsPresented}
        titleVisibility="visible">
        <ConfirmationDialog.Trigger>
          <Button label="Delete" role="destructive" onPress={() => setIsPresented(true)} />
        </ConfirmationDialog.Trigger>
        <ConfirmationDialog.Actions>
          <Button
            label="Delete"
            role="destructive"
            onPress={() => {
              console.log('Deleted');
              setIsPresented(false);
            }}
          />
          <Button label="Cancel" role="cancel" />
        </ConfirmationDialog.Actions>
        <ConfirmationDialog.Message>
          <Text>This action cannot be undone.</Text>
        </ConfirmationDialog.Message>
      </ConfirmationDialog>
    </Host>
  );
}
```

### With message and multiple actions

Use `ConfirmationDialog.Message` to display a descriptive message below the title, and include multiple action buttons for different choices.

```tsx
import { useState } from 'react';
import { Host, ConfirmationDialog, Button, Text } from '@expo/ui/swift-ui';

export default function MultiActionConfirmationDialogExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <ConfirmationDialog
        title="Save Changes?"
        isPresented={isPresented}
        onIsPresentedChange={setIsPresented}
        titleVisibility="visible">
        <ConfirmationDialog.Trigger>
          <Button label="Close Document" onPress={() => setIsPresented(true)} />
        </ConfirmationDialog.Trigger>
        <ConfirmationDialog.Actions>
          <Button label="Save" onPress={() => console.log('Saved')} />
          <Button label="Discard" role="destructive" onPress={() => console.log('Discarded')} />
          <Button label="Cancel" role="cancel" />
        </ConfirmationDialog.Actions>
        <ConfirmationDialog.Message>
          <Text>You have unsaved changes. What would you like to do?</Text>
        </ConfirmationDialog.Message>
      </ConfirmationDialog>
    </Host>
  );
}
```

### Hidden title

Set `titleVisibility="hidden"` to hide the dialog title while still showing the actions and message. You should still provide a `title` for accessibility.

```tsx
import { useState } from 'react';
import { Host, ConfirmationDialog, Button, Text } from '@expo/ui/swift-ui';

export default function HiddenTitleConfirmationDialogExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <ConfirmationDialog
        title="Hidden Title"
        isPresented={isPresented}
        onIsPresentedChange={setIsPresented}
        titleVisibility="hidden">
        <ConfirmationDialog.Trigger>
          <Button label="Show Dialog" onPress={() => setIsPresented(true)} />
        </ConfirmationDialog.Trigger>
        <ConfirmationDialog.Actions>
          <Button label="OK" onPress={() => setIsPresented(false)} />
          <Button label="Cancel" role="cancel" />
        </ConfirmationDialog.Actions>
        <ConfirmationDialog.Message>
          <Text>Only the message and actions are visible.</Text>
        </ConfirmationDialog.Message>
      </ConfirmationDialog>
    </Host>
  );
}
```

## API

```tsx
import { ConfirmationDialog } from '@expo/ui/swift-ui';
```

## Component

### `ConfirmationDialog`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ConfirmationDialogProps](#confirmationdialogprops)\>

`ConfirmationDialog` presents a confirmation dialog with a title, optional message, and action buttons.

> **See:** [https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:message](https://developer.apple.com/documentation/swiftui/view/confirmationdialog\(_:ispresented:titlevisibility:actions:message):)

Props of the `ConfirmationDialog` component.

ConfirmationDialogProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The contents of the confirmation dialog. Should include `ConfirmationDialog.Trigger`, `ConfirmationDialog.Actions`, and optionally `ConfirmationDialog.Message`.

### `isPresented`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean`

Whether the confirmation dialog is presented.

### `onIsPresentedChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(isPresented: boolean) => void`

A callback that is called when the `isPresented` state changes.

### `title`

Supported platforms: iOS, tvOS.

Type: `string`

The title of the confirmation dialog.

### `titleVisibility`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string` • Default: `'automatic'`

The visibility of the dialog title.

Acceptable values are: `'automatic'` | `'hidden'` | `'visible'`

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
