---
title: "AlertDialog"
description: "A Jetpack Compose AlertDialog component for displaying native alert dialogs."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/alertdialog.md"
scraped_at: "2026-07-15T09:00:56.252237"
---

---
title: AlertDialog
description: A Jetpack Compose AlertDialog component for displaying native alert dialogs.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# AlertDialog

A Jetpack Compose AlertDialog component for displaying native alert dialogs.
Android, Included in Expo Go

Expo UI AlertDialog matches the official Jetpack Compose [AlertDialog](https://developer.android.com/develop/ui/compose/components/dialog) API. Content is provided via slot sub-components (`AlertDialog.Title`, `AlertDialog.Text`, `AlertDialog.ConfirmButton`, `AlertDialog.DismissButton`, `AlertDialog.Icon`) that map directly to Compose's slot parameters.

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

### Basic alert dialog

```tsx
import { useState } from 'react';
import { Host, AlertDialog, Button, TextButton, Text } from '@expo/ui/jetpack-compose';

export default function BasicAlertDialogExample() {
  const [visible, setVisible] = useState(false);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Show Alert</Text>
      </Button>
      {visible && (
        <AlertDialog onDismissRequest={() => setVisible(false)}>
          <AlertDialog.Title>
            <Text>Confirm Action</Text>
          </AlertDialog.Title>
          <AlertDialog.Text>
            <Text>Are you sure you want to proceed?</Text>
          </AlertDialog.Text>
          <AlertDialog.ConfirmButton>
            <TextButton onClick={() => setVisible(false)}>
              <Text>Confirm</Text>
            </TextButton>
          </AlertDialog.ConfirmButton>
          <AlertDialog.DismissButton>
            <TextButton onClick={() => setVisible(false)}>
              <Text>Cancel</Text>
            </TextButton>
          </AlertDialog.DismissButton>
        </AlertDialog>
      )}
    </Host>
  );
}
```

### Custom colors

```tsx
import { useState } from 'react';
import { Host, AlertDialog, Button, TextButton, Text } from '@expo/ui/jetpack-compose';

export default function CustomColorsExample() {
  const [visible, setVisible] = useState(false);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Show Alert</Text>
      </Button>
      {visible && (
        <AlertDialog
          onDismissRequest={() => setVisible(false)}
          colors={{
            containerColor: '#1E1E2E',
            titleContentColor: '#CDD6F4',
            textContentColor: '#BAC2DE',
          }}>
          <AlertDialog.Title>
            <Text>Custom Dialog</Text>
          </AlertDialog.Title>
          <AlertDialog.Text>
            <Text>This dialog uses custom colors.</Text>
          </AlertDialog.Text>
          <AlertDialog.ConfirmButton>
            <TextButton onClick={() => setVisible(false)}>
              <Text>OK</Text>
            </TextButton>
          </AlertDialog.ConfirmButton>
          <AlertDialog.DismissButton>
            <TextButton onClick={() => setVisible(false)}>
              <Text>Cancel</Text>
            </TextButton>
          </AlertDialog.DismissButton>
        </AlertDialog>
      )}
    </Host>
  );
}
```

### With icon

```tsx
import { useState } from 'react';
import { Host, AlertDialog, Button, TextButton, Text, Icon } from '@expo/ui/jetpack-compose';

export default function IconDialogExample() {
  const [visible, setVisible] = useState(false);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Show Alert</Text>
      </Button>
      {visible && (
        <AlertDialog onDismissRequest={() => setVisible(false)}>
          <AlertDialog.Icon>
            {/* Replace with your own icon asset */}
            <Icon source={require('./info-icon.xml')} />
          </AlertDialog.Icon>
          <AlertDialog.Title>
            <Text>Dialog with Icon</Text>
          </AlertDialog.Title>
          <AlertDialog.Text>
            <Text>This dialog has an icon above the title.</Text>
          </AlertDialog.Text>
          <AlertDialog.ConfirmButton>
            <TextButton onClick={() => setVisible(false)}>
              <Text>OK</Text>
            </TextButton>
          </AlertDialog.ConfirmButton>
        </AlertDialog>
      )}
    </Host>
  );
}
```

## API

```tsx
import { AlertDialog } from '@expo/ui/jetpack-compose';
```

## Component

### `AlertDialog`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[AlertDialogProps](#alertdialogprops)\>

Renders an `AlertDialog` component with slot-based content matching the Compose API. Content is provided via slot sub-components: `AlertDialog.Title`, `AlertDialog.Text`, `AlertDialog.ConfirmButton`, `AlertDialog.DismissButton`, and `AlertDialog.Icon`.

AlertDialogProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing slot sub-components (`AlertDialog.Title`, `AlertDialog.Text`, `AlertDialog.ConfirmButton`, `AlertDialog.DismissButton`, `AlertDialog.Icon`).

### `colors`

Supported platforms: Android.

Optional • Type: [AlertDialogColors](#alertdialogcolors)

Colors for the alert dialog.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDismissRequest`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the user tries to dismiss the dialog (for example, by tapping outside of it or pressing the back button).

### `properties`

Supported platforms: Android.

Optional • Type: [DialogProperties](#dialogproperties)

Properties for the dialog window.

### `tonalElevation`

Supported platforms: Android.

Optional • Type: `number`

The tonal elevation of the dialog in dp, which affects its background color based on the color scheme.

## Types

### `AlertDialogColors`

Supported platforms: Android.

Colors for the alert dialog, matching `AlertDialogDefaults` in Compose.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the dialog. |
| iconContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of the icon. |
| textContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of the body text. |
| titleContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of the title text. |

### `DialogProperties`

Supported platforms: Android.

Properties for the dialog window, matching `DialogProperties` in Compose.

| Property | Type | Description |
| --- | --- | --- |
| decorFitsSystemWindows(optional) | `boolean` | Whether the dialog's decor fits system windows (status bar, navigation bar, and more). When `true`, the dialog's content will be inset to avoid overlapping with system UI. Default: `true` |
| dismissOnBackPress(optional) | `boolean` | Whether the dialog can be dismissed by pressing the back button. Default: `true` |
| dismissOnClickOutside(optional) | `boolean` | Whether the dialog can be dismissed by clicking outside of it. Default: `true` |
| usePlatformDefaultWidth(optional) | `boolean` | Whether the dialog should use the platform default width. Default: `true` |
